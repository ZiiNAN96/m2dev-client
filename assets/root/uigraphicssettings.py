# -*- coding: utf-8 -*-
import ui
import systemSetting
import chat

PRESETS = ("Niedrig", "Mittel", "Hoch", "Ultra", "Benutzerdefiniert")
STYLES = ("Klassisch", "Modern")
VEGETATION = ("Niedrig", "Mittel", "Hoch", "Ultra")
FOG = ("Dicht", "Mittel", "Leicht")
SHADOWS = ("Aus", "Niedrig", "Mittel", "Hoch", "Ultra")
SHADOW_VALUES = (0, 1, 3, 4, 5)
AO = ("Aus", "Niedrig", "Hoch")
BLOOM = ("Aus", "Ein")
ATMOSPHERE = ("Niedrig", "Hoch")
MIN_DISTANCE = 6400.0
MAX_DISTANCE = 38400.0


class GraphicsComboBox(ui.ComboBox):
    def __init__(self, closeOthers):
        ui.ComboBox.__init__(self)
        self.AddFlag("float")
        self.closeOthers = ui.__mem_func__(closeOthers)

    def OnMouseLeftButtonUp(self):
        if not self.isListOpened:
            self.closeOthers(self)
            self.SetTop()
        ui.ComboBox.OnMouseLeftButtonUp(self)

    def Destroy(self):
        self.closeOthers = None
        ui.ComboBox.Destroy(self)


class GraphicsDialog(ui.BoardWithTitleBar):
    def __init__(self):
        ui.BoardWithTitleBar.__init__(self)
        self.AddFlag("movable")
        self.AddFlag("float")
        self.SetSize(360, 552)
        self.SetTitleName("Grafikeinstellungen")
        self.SetCloseEvent(ui.__mem_func__(self.Close))
        self.controls = []
        self.combos = []
        self.dirty = False
        self.refreshing = False
        self.closeEvent = None
        self.preset = self.MakeCombo("Grafikqualit\xe4t", 45, PRESETS, self.OnPreset)
        self.Text("Qualit\xe4t, Schatten, AO und Sichtweite.", 20, 73)
        self.style = self.MakeCombo("Grafik und Licht", 96, STYLES, self.OnStyle)
        self.Text("Modern: Beleuchtung und Oberfl\xe4chen.", 20, 124)
        self.vegetation = self.MakeCombo("Vegetation", 147, VEGETATION, self.OnVegetation)
        self.Text("H\xf6here Stufen halten Details l\xe4nger sichtbar.", 20, 175)
        self.Text("Sichtweite", 20, 209)
        self.distance = ui.SliderBar()
        self.distance.SetParent(self)
        self.distance.SetPosition(165, 211)
        self.distance.SetEvent(ui.__mem_func__(self.OnDistance))
        self.distance.Show()
        self.distanceText = self.Text("", 20, 232)
        self.fog = self.MakeCombo("Nebel", 261, FOG, self.OnFog)
        self.shadows = self.MakeCombo("Sonnenschatten", 296, SHADOWS, self.OnShadows)
        self.ao = self.MakeCombo("Umgebungsverdeckung", 332, AO, self.OnAO)
        self.bloom = self.MakeCombo("Bloom", 368, BLOOM, self.OnBloom)
        self.sky = self.MakeCombo("Himmelqualit\xe4t", 404, ATMOSPHERE, self.OnSky)
        self.fogQuality = self.MakeCombo("Nebelqualit\xe4t", 440, ATMOSPHERE, self.OnFogQuality)
        self.Text("Licht, Schatten und Atmosph\xe4re: Modus Modern.", 20, 481)
        self.Text("\xc4nderungen werden sofort angewendet.", 20, 518)
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
        self.Text(label, 20, y + 4)
        combo = GraphicsComboBox(self.CloseOtherCombos)
        combo.SetParent(self)
        combo.SetPosition(165, y)
        combo.SetSize(175, 22)
        for index, name in enumerate(choices):
            combo.InsertItem(index, name)
        combo.SetEvent(ui.__mem_func__(event))
        combo.Show()
        self.combos.append(combo)
        return combo

    def CloseOtherCombos(self, selected):
        for combo in self.combos:
            if combo is not selected:
                combo.CloseListBox()

    def Refresh(self, updateDistance=True):
        self.refreshing = True
        try:
            values = systemSetting.GetGraphicsSettings()
            self.preset.SetCurrentItem(PRESETS[values["preset"]])
            self.style.SetCurrentItem(STYLES[values["style"]])
            self.vegetation.SetCurrentItem(VEGETATION[values["vegetation"]])
            self.fog.SetCurrentItem(FOG[values["fogLevel"]])
            shadow = values["shadows"]
            self.shadows.SetCurrentItem(SHADOWS[SHADOW_VALUES.index(1 if shadow == 2 else shadow)])
            self.ao.SetCurrentItem(AO[values["ambientOcclusion"]])
            self.bloom.SetCurrentItem(BLOOM[values["bloom"]])
            self.sky.SetCurrentItem(ATMOSPHERE[values["modernSky"]])
            self.fogQuality.SetCurrentItem(ATMOSPHERE[values["highQualityFog"]])
            if updateDistance:
                self.distance.SetSliderPos((values["viewDistance"] - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE))
            self.distanceText.SetText("Sichtweite: %d%% (passt sich der Last an)" % (values["viewDistance"] * 100.0 / 25600.0))
        finally:
            self.refreshing = False

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

    def OnFogQuality(self, index):
        self.Apply("highQualityFog", index)

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
        self.closeEvent = None
        for combo in self.combos:
            combo.CloseListBox()
            combo.Destroy()
        self.combos = []
        self.controls = []
        self.preset = self.style = self.vegetation = self.fog = None
        self.shadows = self.ao = self.bloom = self.sky = self.fogQuality = None
        self.distance = self.distanceText = None
        self.Hide()
