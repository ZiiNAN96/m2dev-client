# -*- coding: utf-8 -*-
import ui
import systemSetting
import chat
import uiCommon
import wndMgr

PRESETS = ("Niedrig", "Mittel", "Hoch", "Ultra", "Benutzerdefiniert")
STYLES = ("Klassisch", "Modern")
VEGETATION = ("Niedrig", "Mittel", "Hoch", "Ultra")
FOG = ("Dicht", "Mittel", "Leicht")
SHADOWS = ("Aus", "Niedrig", "Mittel", "Hoch", "Ultra")
SHADOW_VALUES = (0, 1, 3, 4, 5)
AO = ("Aus", "Niedrig", "Hoch")
BLOOM = ("Aus", "Ein")
ATMOSPHERE = ("Niedrig", "Hoch")
WATER = ("Niedrig", "Mittel", "Hoch", "Ultra")
FRAME_RATE_LIMITS = ("60", "120", "Unbegrenzt")
VSYNC = ("Aus", "Ein")
DISPLAY_MODES = ("Fenster", "Randloses Vollbild")
MIN_DISTANCE = 6400.0
MAX_DISTANCE = 38400.0


class GraphicsComboBox(ui.ComboBox):
    def __init__(self, closeOthers):
        ui.ComboBox.__init__(self)
        self.AddFlag("float")
        self.closeOthers = ui.__mem_func__(closeOthers)
        self.prepareOpen = None
        self.scroll = ui.ScrollBar()
        self.scroll.SetParent(self.listBox)
        self.scroll.SetScrollEvent(ui.__mem_func__(self.OnScroll))
        self.scroll.Hide()

    def OnMouseLeftButtonUp(self):
        if not self.isListOpened:
            if self.prepareOpen:
                self.prepareOpen()
            self.closeOthers(self)
            self.SetTop()
        ui.ComboBox.OnMouseLeftButtonUp(self)
        if self.isListOpened:
            count = self.listBox.GetItemCount()
            height = min(8, count) * self.listBox.stepSize
            self.listBox.SetSize(self.width, height)
            self.listBox.SetBasePos(0)
            if count > 8:
                self.scroll.SetPosition(self.width - 15, 0)
                self.scroll.SetScrollBarSize(height)
                self.scroll.SetMiddleBarSize(8.0 / count)
                self.scroll.SetPos(0)
                self.scroll.Show()
            else:
                self.scroll.Hide()

    def OnScroll(self):
        self.listBox.SetBasePos(int(self.scroll.GetPos() * max(0, self.listBox.GetItemCount() - 8)))

    def Destroy(self):
        self.closeOthers = None
        self.prepareOpen = None
        self.scroll = None
        ui.ComboBox.Destroy(self)


class GraphicsDialog(ui.BoardWithTitleBar):
    def __init__(self):
        ui.BoardWithTitleBar.__init__(self)
        self.AddFlag("movable")
        self.AddFlag("float")
        self.SetSize(700, 510)
        self.SetTitleName("Grafikeinstellungen")
        self.SetCloseEvent(ui.__mem_func__(self.Close))
        self.controls = []
        self.combos = []
        self.dirty = False
        self.refreshing = False
        self.closeEvent = None
        self.changeEvent = None
        self.confirmation = None
        self.lastDisplay = None
        self.lastSeconds = -1
        self.windowResolution = None
        self.preset = self.MakeCombo("Grafikqualit\xe4t", 45, PRESETS, self.OnPreset)
        self.Text("Qualit\xe4t, Schatten, AO und Sichtweite.", 20, 73)
        self.style = self.MakeCombo("Grafik und Licht", 90, STYLES, self.OnStyle)
        self.Text("Modern: Beleuchtung und Oberfl\xe4chen.", 20, 118)
        self.vegetation = self.MakeCombo("Vegetation", 135, VEGETATION, self.OnVegetation)
        self.Text("H\xf6here Stufen halten Details l\xe4nger sichtbar.", 20, 163)
        self.Text("Sichtweite", 20, 194)
        self.distance = ui.SliderBar()
        self.distance.SetParent(self)
        self.distance.SetPosition(165, 196)
        self.distance.SetEvent(ui.__mem_func__(self.OnDistance))
        self.distance.Show()
        self.distanceText = self.Text("", 20, 218)
        self.fog = self.MakeCombo("Nebel", 248, FOG, self.OnFog)
        self.shadows = self.MakeCombo("Sonnenschatten", 281, SHADOWS, self.OnShadows)
        self.ao = self.MakeCombo("Umgebungsverdeckung", 314, AO, self.OnAO)
        self.bloom = self.MakeCombo("Bloom", 347, BLOOM, self.OnBloom)
        self.sky = self.MakeCombo("Himmelqualit\xe4t", 380, ATMOSPHERE, self.OnSky)
        self.water = self.MakeCombo("Wasserqualit\xe4t", 413, WATER, self.OnWater)
        self.Text("Licht, Schatten und Wasser: Modus Modern.", 20, 446)
        self.Text("ANZEIGEEINSTELLUNGEN", 380, 45)
        self.resolution = self.MakeDisplayCombo("Aufl\xf6sung", 83, (), self.OnResolution)
        self.resolution.prepareOpen = ui.__mem_func__(self.RefreshDisplayOptions)
        self.displayMode = self.MakeDisplayCombo("Anzeigemodus", 153, DISPLAY_MODES, self.OnDisplayMode)
        self.Text("Randlos verwendet die Desktop-Aufl\xf6sung.", 380, 210)
        self.frameRateLimit = self.MakeDisplayCombo("FPS-Limit", 245, FRAME_RATE_LIMITS, self.OnFrameRateLimit)
        self.vsync = self.MakeDisplayCombo("VSync", 315, VSYNC, self.OnVSync)
        self.Text("Anzeigewechsel: 15 Sekunden zum Best\xe4tigen.", 380, 390)
        self.Text("Ohne Best\xe4tigung wird zur\xfcckgesetzt.", 380, 410)
        self.Text("\xc4nderungen werden sofort angewendet.", 20, 477)
        self.Refresh()
        self.SetCenterPosition()

    def Text(self, text, x, y, disabled=False):
        label = ui.TextLine()
        label.SetParent(self)
        label.SetPosition(x, y)
        label.SetText(text)
        if disabled:
            label.SetFontColor(0.6, 0.6, 0.6)
        label.Show()
        self.controls.append(label)
        return label

    def MakeCombo(self, label, y, choices, event):
        caption = self.Text(label, 20, y + 4)
        combo = GraphicsComboBox(self.CloseOtherCombos)
        combo.label = caption
        combo.SetParent(self)
        combo.SetPosition(165, y)
        combo.SetSize(175, 22)
        for index, name in enumerate(choices):
            combo.InsertItem(index, name)
        combo.SetEvent(ui.__mem_func__(event))
        combo.Show()
        self.combos.append(combo)
        return combo

    def MakeDisplayCombo(self, label, y, choices, event):
        combo = self.MakeCombo(label, y, choices, event)
        combo.label.SetPosition(380, y)
        combo.SetPosition(380, y + 24)
        combo.SetSize(300, 22)
        return combo

    def RefreshDisplayOptions(self):
        options = systemSetting.GetDisplayOptions()
        values = systemSetting.GetGraphicsSettings()
        self.resolutions = options["resolutions"]
        self.resolution.ClearItem()
        for index, (width, height) in enumerate(self.resolutions):
            self.resolution.InsertItem(index, "%d \xd7 %d" % (width, height))
        if values["displayMode"] == 1:
            self.resolution.Disable()
        else:
            self.resolution.Enable()
            self.windowResolution = (values["resolutionWidth"], values["resolutionHeight"])
        self.resolution.SetCurrentItem("%d \xd7 %d" % (values["resolutionWidth"], values["resolutionHeight"]))
        self.displayMode.SetCurrentItem(DISPLAY_MODES[values["displayMode"]])
        self.lastDisplay = (values["resolutionWidth"], values["resolutionHeight"], values["displayMode"])

    def OnResolution(self, index):
        width, height = self.resolutions[index]
        self.ApplyDisplay({"resolutionWidth": width, "resolutionHeight": height})

    def OnDisplayMode(self, index):
        values = {"displayMode": index}
        if index == 0:
            options = systemSetting.GetDisplayOptions()
            width, height = self.windowResolution or options["resolutions"][-1]
            if (width, height) not in options["resolutions"]:
                width, height = options["resolutions"][-1]
            values.update(resolutionWidth=width, resolutionHeight=height)
        self.ApplyDisplay(values)

    def ApplyDisplay(self, values):
        self.CloseOtherCombos(None)
        if not systemSetting.ApplyGraphicsSettings(values):
            chat.AppendChat(chat.CHAT_TYPE_INFO, "Anzeigewechsel nicht verf\xfcgbar. Laufende Best\xe4tigung abschlie\xdfen.")
        self.RefreshDisplayOptions()

    def ConfirmDisplay(self):
        if systemSetting.ConfirmDisplaySettings():
            self.dirty = False
            self.CloseConfirmation()
        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, "Anzeigeeinstellungen konnten nicht gespeichert werden.")
        return True

    def CancelDisplay(self):
        systemSetting.CancelDisplaySettings()
        self.CloseConfirmation()
        return True

    def CloseConfirmation(self):
        if self.confirmation:
            self.confirmation.Close()
            self.confirmation = None
        self.lastSeconds = -1

    def OnUpdate(self):
        values = systemSetting.GetGraphicsSettings()
        state = (values["resolutionWidth"], values["resolutionHeight"], values["displayMode"])
        if state != self.lastDisplay:
            self.RefreshDisplayOptions()
            self.SetCenterPosition()
        seconds = systemSetting.GetDisplayConfirmationSeconds()
        if seconds:
            if not self.confirmation:
                self.CloseOtherCombos(None)
                self.SetCenterPosition()
                self.confirmation = uiCommon.QuestionDialog()
                self.confirmation.SetAcceptText("Beibehalten")
                self.confirmation.SetCancelText("Zur\xfcck")
                self.confirmation.SetAcceptEvent(ui.__mem_func__(self.ConfirmDisplay))
                self.confirmation.SetCancelEvent(ui.__mem_func__(self.CancelDisplay))
                self.confirmation.OnPressEscapeKey = ui.__mem_func__(self.CancelDisplay)
                self.confirmation.SetText("Diese Anzeigeeinstellungen beibehalten?")
                self.confirmation.SetWidth(380)
                self.confirmation.countdown = ui.TextLine()
                self.confirmation.countdown.SetParent(self.confirmation)
                self.confirmation.countdown.SetWindowHorizontalAlignCenter()
                self.confirmation.countdown.SetHorizontalAlignCenter()
                self.confirmation.countdown.SetPosition(0, 48)
                self.confirmation.countdown.Show()
                self.confirmation.Open()
            if seconds != self.lastSeconds:
                self.confirmation.countdown.SetText("Automatisch zur\xfcck in %d Sekunden." % seconds)
                self.lastSeconds = seconds
        elif self.confirmation:
            self.CloseConfirmation()

    def CloseOtherCombos(self, selected):
        for combo in self.combos:
            if combo is not selected:
                combo.CloseListBox()

    def Refresh(self, updateDistance=True):
        self.refreshing = True
        try:
            values = systemSetting.GetGraphicsSettings()
            self.RefreshDisplayOptions()
            self.preset.SetCurrentItem(PRESETS[values["preset"]])
            self.style.SetCurrentItem(STYLES[values["style"]])
            self.vegetation.SetCurrentItem(VEGETATION[values["vegetation"]])
            self.fog.SetCurrentItem(FOG[values["fogLevel"]])
            shadow = values["shadows"]
            self.shadows.SetCurrentItem(SHADOWS[SHADOW_VALUES.index(1 if shadow == 2 else shadow)])
            self.ao.SetCurrentItem(AO[values["ambientOcclusion"]])
            self.bloom.SetCurrentItem(BLOOM[values["bloom"]])
            self.sky.SetCurrentItem(ATMOSPHERE[values["modernSky"]])
            self.water.SetCurrentItem(WATER[values["water"]])
            self.frameRateLimit.SetCurrentItem(FRAME_RATE_LIMITS[values["frameRateLimit"]])
            self.vsync.SetCurrentItem(VSYNC[values["vsync"]])
            if values["style"] == 0:
                self.fog.Show()
                self.fog.label.Show()
            else:
                self.fog.CloseListBox()
                self.fog.Hide()
                self.fog.label.Hide()
            if updateDistance:
                self.distance.SetSliderPos((values["viewDistance"] - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE))
            self.distanceText.SetText("Sichtweite: %d%% (passt sich der Last an)" % (values["viewDistance"] * 100.0 / 25600.0))
        finally:
            self.refreshing = False
        if self.changeEvent:
            self.changeEvent()

    def OnPreset(self, index):
        if systemSetting.ApplyGraphicsPreset(index):
            self.dirty = True
        self.Refresh()

    def Apply(self, option, value, updateDistance=True):
        if systemSetting.ApplyGraphicsSettings({option: value}):
            self.dirty = True
        self.Refresh(updateDistance)

    def OnVegetation(self, index):
        self.Apply("vegetation", index)

    def OnStyle(self, index):
        self.Apply("style", index)

    def OnShadows(self, index):
        self.Apply("shadows", SHADOW_VALUES[index])

    def OnAO(self, index):
        self.Apply("ambientOcclusion", index)

    def OnBloom(self, index):
        self.Apply("bloom", index)

    def OnSky(self, index):
        self.Apply("modernSky", index)

    def OnWater(self, index):
        self.Apply("water", index)

    def OnFrameRateLimit(self, index):
        self.Apply("frameRateLimit", index)

    def OnVSync(self, index):
        self.Apply("vsync", index)

    def OnDistance(self):
        if self.refreshing:
            return
        # A pressed native DragButton fires OnMove from SetPosition. Do not reposition
        # it recursively while handling that event; only refresh labels/other options.
        self.Apply("viewDistance", MIN_DISTANCE + self.distance.GetSliderPos() * (MAX_DISTANCE - MIN_DISTANCE), False)

    def OnFog(self, index):
        self.Apply("fogLevel", index)

    def Open(self):
        self.Refresh()
        self.Show()
        self.SetTop()

    def Close(self):
        self.CancelDisplay()
        for combo in self.combos:
            combo.CloseListBox()
        if self.dirty:
            if not systemSetting.SaveGraphicsSettings():
                chat.AppendChat(chat.CHAT_TYPE_INFO, "Grafikeinstellungen konnten nicht gespeichert werden.")
                return
            self.dirty = False
        self.Hide()
        if self.closeEvent:
            self.closeEvent()

    def OnPressEscapeKey(self):
        self.Close()
        return True

    def Destroy(self):
        self.CancelDisplay()
        self.resolution = self.displayMode = None
        self.closeEvent = None
        self.changeEvent = None
        for combo in self.combos:
            combo.CloseListBox()
            combo.Destroy()
        self.combos = []
        self.controls = []
        self.preset = self.style = self.vegetation = self.fog = None
        self.shadows = self.ao = self.bloom = self.sky = self.water = None
        self.frameRateLimit = self.vsync = None
        self.distance = self.distanceText = None
        self.Hide()
