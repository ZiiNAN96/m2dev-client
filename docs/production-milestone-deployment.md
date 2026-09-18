> Aktuelles Performance-Deployment vom 17.09.2026: **P0-L FINAL = GO**, siehe [Production-Deployment unten](#p0-l-final-production-deployment--17092026). Frischer Release aus Source `80f7739`, Python `fabe7737`, Originalclient-Smoke A1 → B1 → A1 bestanden. Die frühere H2-Abnahme und ihre damaligen Grenzen bleiben als historischer Nachweis erhalten.
>
> Texturstand: [Alle Bodentexturen wieder original; flächiges 3D-Gras abgeschaltet](terrain-original-restoration.md). Die folgenden H2-EXE-Hashes und Gras-Erzeugung beschreiben den früheren Stand.

# H2-X-FINAL: Production-Milestone-Audit

Stand: 16.09.2026. **Dateideployment und zwei Originalläufe geprüft; Nutzer-Sichtabnahme bestätigt. Finale H2-/Production-Abnahme noch NO-GO, weil der geforderte Mapwechsel in den Originallogs fehlt und die Abweichung zur pauschalen Nutzerbestätigung noch zu klären ist.** Testclient-Nachweise ersetzen diesen Punkt nicht. Kein Commit und kein Push, solange das vollständige FINAL GO fehlt.

## Ausgangspunkt und Identität

| Bereich | Pfad / Stand |
| --- | --- |
| Production Source | `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client-src` |
| Source Branch / HEAD | `codex/g56-hdr-atmosphere` / `02e0ec7` |
| Originalclient | `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client` |
| Runtime Branch / HEAD | `codex/g56-hdr-colors` / `6c713237` |
| Tatsächlich frisch gestartete Datei | `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client\Metin2_Release.exe` |
| Working Directory | Originalclient-Verzeichnis, kein Testclient |
| Zusatzargument | `--renderer-diagnostics`, ausschließlich vorhandene Protokollierung; normales `prototype.py`, normaler Netzwerklogin |

`Metin2.exe` existiert hier nicht; die normale Release-Datei heißt `Metin2_Release.exe`. Der frische Lauf mit PID 10816 startete am 16.09.2026 um 13:21:03 (Wien), erreichte den echten Spielbetrieb auf C1 und endete um 13:21:59 mit Exit 0. Prozesspfad, Start, Exit, Lifecycle und Original-Logs wurden zusammen gesichert.

Die offenen Source-Änderungen entsprechen dem vorher geprüften H2-Stand. Der SHA256-Abgleich der 51 in `grass-preload/result.json` erfassten Dateien findet nur zwei nachträglich ergänzte H2-Dokumente; keine Änderung der dort erfassten Implementierung, Tests oder Assets. `PackContentAudit` war bereits Teil des vorherigen Deployments. In diesem Audit wurde keine funktionale Produktionsquelle verändert.

Die offenen Runtime-Änderungen umfassen das dokumentierte H2-Deployment sowie nachfolgende Grafikpräferenzen und Logs. `config/graphics.cfg` war beim Audit bereits **Custom / Modern**, Vegetation High, AO High, Wasser Ultra, HDR/Bloom/Himmel aktiv, Sichtweite 25600, Fog 0. Diese Nutzerwerte wurden gesichert und nicht durch pauschale Presetkopien ersetzt. `config/metin2.cfg` enthielt bereits Shadow 4 und Fog 0.

## EXE- und Paketabgleich

| Datei | Bytes | Dateizeit (Wien) | SHA256 |
| --- | ---: | --- | --- |
| Original `Metin2_Release.exe` | 31.099.904 | 16.09.2026 11:59:22 | `959d03d5ff6e560a2043e300688811852ff56784d14236aea541a0ab003964cd` |
| Original `Metin2_Debug.exe`, nach Korrektur | 43.063.808 | 16.09.2026 12:05:36 | `7e969342228a6428bfa2cdb65299d3429a813c1ee565b3c4dd34ed28731e0cff` |
| Original `pack/root.pck` | 6.778.061 | 16.09.2026 12:43:25 | `0c1c6f47e6dce89d912363882789d76b3cfe1395cad0290e2b59a7d434092994` |

Release und Debug stimmen bytegenau mit `m2dev-client-src/build-h2x/msvc/bin/Release/Metin2_Release.exe` beziehungsweise `.../Debug/Metin2_Debug.exe` sowie den Binärhashes des abgeschlossenen H2-Gras-Gates überein. Release stimmt auch mit `build-h2x/runtime-manual/Metin2_Release.exe`, `runtime-grass-preload-final/Metin2_Release.exe` und `runtime-deployment-check/Metin2_Release.exe` überein.

Ältere G8-Binaries bleiben als Vergleichsartefakte im Source-Buildbaum: Release SHA256 `4c362615c0b3b008a95f574a7e3591ad7059cee95cf96e3e681ea818c0212a8c`, Debug `082982302bcf61dfe51a26b33d01a4a16029072ec9fe55de63e62e19f35db177`. Sie werden nicht als Originalclient gestartet. Das vollständige Inventar enthält 40 Build-/Test-EXEs mit absoluten Pfaden, Größe, Zeit und Hash.

## Gefundene und geschlossene Deployment-Lücke

Die alte Originaldatei `Metin2_Debug.exe` vom 03.09.2026 war noch nicht aktualisiert. Ihr SHA256 war `638f93e3db8baaa7e63b1ffe36932c930f744a8623a80c66c391299c033c380e`; sie importierte `d3d9.dll` und `d3dx9_43.dll`. Diese startbare alte Variante widersprach dem Zero-Legacy-Ziel des Originalordners.

Am 16.09.2026 um 13:23:22 wurde ausschließlich diese Debug-Datei durch den bereits geprüften H2-Debug-Build ersetzt. Die alte Datei wurde vorher kopiert und die Sicherung per SHA256 bestätigt. Backup: `m2dev-client-src/build-h2x/production-final-20260916/before-runtime/Metin2_Debug.exe`. Der neue Zielhash wurde geprüft. Ein erster Dateiaustauschversuch scheiterte vor dem Austausch an einem leeren Backup-Pfad; die geprüfte Zwischenkopie wurde danach erfolgreich auf den expliziten Zielpfad verschoben.

Release-EXE, Root-Paket und Assets benötigten keine erneute Kopie. Nach dem Debug-Austausch wurde die normale Release-Datei erneut aus dem Originalordner gestartet. Der Debug-Build selbst wurde in diesem Audit nicht erneut ingame ausgeführt; sein vorhandenes 72/72-Gate bleibt der Funktionsnachweis.

## Runtime- und Assetvergleich

- **342/342 Root-Dateien identisch** mit dem freigegebenen Deploymentplan: 87 bisherige Quellen und 255 hinzugefügte Vegetations-/Texturquellen.
- Der frisch ausgeführte `PackContentAudit source` dekodierte alle 342 Einträge aus dem tatsächlich installierten `pack/root.pck`: **0 Unterschiede, 0 zusätzliche Quelldateien**.
- `uigraphicssettings.py` und `uisystemoption.py` sind damit im tatsächlich geladenen Paket enthalten; Classic/Modern, fünf Presets, Vegetation, Schatten, AO, Bloom, Himmel und Wasser sind in der vorhandenen UI verdrahtet.
- Registry: 118 Legacy-Zuordnungen. Originalordner: 121 GLB-Dateien in den Assetquellen (118 konvertierte Legacy-Typen und drei H2-Demonstratoren), zugehörige ZVEG-Metadaten und die sechs Materialtexturen unter ihren virtuellen Pfaden.
- Alle anderen im Deploymentplan erfassten Pakete und Root-Quellen stimmen weiterhin mit dessen Hashes überein. Die einzigen Abweichungen gegen den damaligen Dateiplan sind das hier aktualisierte Debug-EXE sowie die bereits vorgefundenen beiden Grafik-Konfigurationen.
- Modern-, Water- und Atmosphere-Shader werden aus eingebetteten C++-Shaderquellen und dem DiligentFX-Shader-Factory-Pfad erzeugt. Es fehlt kein separates testclientlokales Shaderverzeichnis. Environment-, Wasser- und Legacy-Effektcontent bleibt in den bestehenden Paketen.

## Testclient gegen Originalclient

28 vorhandene Test-Root-Verzeichnisse unter G8/H2 wurden gegen die Originalquellen verglichen. Alle finalen Grafik-UI-Dateien stimmen überein. Unterschiede:

1. Diagnostische `prototype.py`-Dateien laden Kamera-, Map-, Effekt- oder Performance-Testserien. Der Originalclient behält das normale Netzwerk-Startskript.
2. Im älteren `build-h2x/runtime-native/` weichen zwei Impostor-Texturen vom finalen Stand ab. Die finalen H2-Verzeichnisse und der Originalclient besitzen bereits die neueren identischen Dateien. Die alten Testtexturen werden nicht deployt.
3. F5-Character-Fixtures sind Testcontent. Die freigegebene F5-Implementierung ist Bestandteil der Production-EXE; F5 beinhaltete ausdrücklich keine Migration der normalen Player/Mobs zu GLB. Ein animierter GLB-Actor wurde im hier beobachteten Originalclient-Lauf nicht geladen. Das ist eine offene konkrete Runtime-Abdeckung, kein Anlass, experimentelle Characters zu deployen.

Kein weiterer fehlender freigegebener Runtime-/Assetbestand wurde im geprüften Dateiumfang gefunden. Diese Dateiaussage ist keine vollständige visuelle Featureabnahme.

## Milestone-Matrix

„Build vorhanden“ bezeichnet die geprüfte finale H2-EXE, welche die früheren Meilensteine enthält. „Deployed“ ist durch identische EXE-/Paket-/Quelldaten belegt. Runtime-Zähler und visuelle Abnahme werden getrennt bewertet.

| Milestone | Source vorhanden | Production Build vorhanden | Originalclient deployed | Runtime Proof im Originalclient | Nur Testclient? | Status |
| --- | --- | --- | --- | --- | --- | --- |
| F3/4-X | Ja | Ja | Ja | 880 native GR2-Reads, 50.511 unabhängige Posesamples, 46.987 GPU-Frames; Granny-Reads/CPU-Deformation/Fallbacks 0 | Nein | Produktionspfad bestätigt |
| H-X | Ja | Ja | Ja | Registry 118, 161 erstellte Vegetationsinstanzen, Bäume sichtbar, VegetationFailures 0 | Nein | Produktionspfad bestätigt |
| F5-X | Ja, gemeinsames RuntimeSkeleton/RuntimeAnimationClip/RuntimeAnimationInstance | Ja | Ja, Implementierung | Normaler GR2-Pfad bestätigt; animierter GLB-Actor in diesem Lauf NOT RUN | Implementierung nein; Character-Fixture ja | Deployed; direkte Originalclient-GLB-Abdeckung offen |
| G0-X | Ja | Ja | Ja, beide UI-Module im verifizierten Root-Paket | Gespeicherte Modern-/Custom-Konfiguration aktiv; Nutzer bestätigt Menü und Schalter | Nein | Deployed; manuell bestätigt |
| G-DX / G-DX-C | Ja | Ja | Ja | 419.655 Shadow-Draws, 5.034 PBR-Material-Draws, AO-Submit aktiv; gemeinsame Beleuchtung | Nein | Renderpfade aktiv; Nutzer-Sichtabnahme bestätigt |
| G5/6-X | Ja | Ja | Ja | 984 Tone-Mapped Frames, HDR-Target, Bloom/Atmosphere-Submit aktiv, 7.712 Shimmer-Draws; blaue Aura und Effekte sichtbar | Nein | Technische Pfade und Nutzer-Sichtabnahme bestätigt |
| G7-X | Ja | Ja | Ja | 10.621 Water-Draws, 984 SSR-Frames, SSR-Fallbacks 0 | Nein | Water/SSR aktiv; Nutzer-Sichtabnahme bestätigt |
| G8-X | Ja, HEAD `02e0ec7` | Ja | Ja | Finaler Renderer-/Assetstand identisch; farbige Welt/Player/Mobs im C1-Bild | Nein | Deployed; Nutzer-Sichtabnahme bestätigt |
| H2-X | Ja | Ja | Ja | Gras auf C1 beim Laden, 20/20 Tiles, 539.411 Platzierungen; Instancing/LOD/Impostor-Draws und saubere Freigabe | Nein | Teilweise bestätigt; FINAL GO offen |

## Frischer Originalclient-Smoke

Der erste Lauf benutzt den regulären Originalordner und keine geänderten Startskripte. `gdxc-lifecycle.log` belegt **Start → HandShake → Login → Select → Loading → Game → WorldReadyForPresent → WorldPresented → ShutdownClean**. Dies ist echter Netzwerk-/Originalclientbetrieb, kein Offline-Harness. Die wiederholten Login/Select-Phasen vor dem ersten Weltbild werden nicht als abgeschlossener Ingame-Relog gezählt.

Das selbst geprüfte Bild `01-original-ingame.png` zeigt C1, Player mit blauer Aura, Mobs, Bäume, Terrain und vorhandenes Gras. Es ist ein Standbild: zeitlicher Wind, weicher Fade und fehlendes Nachspawnen sind damit noch nicht abgenommen.

| Punkt | Ergebnis |
| --- | --- |
| Normaler frischer Start, Login/Select/Ingame | PASS, normaler Pfad und Lifecycle |
| Grass Preparation beim C1-Laden | PASS: 20/20 Tiles, 539.411 Platzierungen, 28.232 Zellen, 17.261.152 Byte Platzierungsdaten, 76,816 ms |
| Vorbereitungsort vor Weltbild | Source `CMapOutdoor::Load` ruft `PrepareNativeGrass` auf; Originallog bestätigt den vollständigen Lauf |
| Mehrere hundert Meter Bewegung/Rückkehr ohne Nachspawnen | Nutzer bestätigt fehlerfreie manuelle Prüfung; keine autonome kontinuierliche Videoabnahme |
| High 100 m / weicher Fade | Freigegebener Binär-/Sourcewert vorhanden; Nutzer bestätigt fehlerfreie manuelle Prüfung |
| A1 → B1 → A1 oder zwei echte Maps mit Rückkehr | NOT RUN im Originalclient; bisher nur C1 |
| LOD/Impostors/Sharing | Runtime-Draws und Instanzuploads aktiv; Nutzer bestätigt fehlerfreie Sichtprüfung |
| Branch-/Leaf-/Grass-Wind | Implementierung vorhanden; Nutzer bestätigt fehlerfreie Sichtprüfung |
| Sonne/Foliage/Two-sided/Transmission | Gemeinsamer `SceneLighting.sun`-Pfad vorhanden; Nutzer bestätigt fehlerfreie Sichtprüfung |
| Water/G8/Legacy-Farben | Technische Pfade aktiv, C1-Standbild geprüft; Nutzer bestätigt fehlerfreie Sichtprüfung |
| Ingame-Logout/Relog | NOT RUN |
| Normaler Exit | PASS: Exit 0 und ShutdownClean |

## Nullzähler und Zero Legacy

Frischer Source-/Link-/Build-Binäraudit: PASS, 1.505 Production-Dateien, 43 transitive Linkprojekte, vier Build-Binaries, Source-/SDK-/Linktreffer jeweils 0. Zusätzlicher Import-/SDK-Marker-Scan beider tatsächlich installierten Client-EXEs: **D3D9 = 0, Granny = 0, SpeedTree = 0** nach dem Debug-Austausch. Im Originalordner wurden keine Runtime-DLL-Dateien gefunden. Alte SDK-Header im Sourcebaum sind keine gelinkte Runtime; `DDRAW.dll` als bestehende Importabhängigkeit ist kein D3D9-Renderer.

Frischer erster Originalclient-Lauf:

- `DiligentErrors=0`, `DiligentFatals=0`, `AllCPUDeformationCalls=0`, `AllCPUDeformationVertices=0`, `GPUFallbacks=0`.
- `VegetationFailures=0`, `SkinPreparationFailures=0`, `AnimationRuntimeFailures=0`, `GrannyFileReads=0`.
- Nach Shutdown: SourceTextures/SourceBuffers, SkinMeshes/BoneRemaps/BonePalettes, CollisionResources, VegetationAssets/Instances/RenderAssets/Geometry/InstanceBuffers/InstanceBytes, AssetDocuments/AnimationInstances/MeshBindings, GR2ReaderResources, IndependentAnimationInstances, RuntimeSkeletons/RuntimeAnimationClips und PrototypeGeometry/PrototypePalettes jeweils **0**.
- Terrain-Owner meldet Text/UI/Water/World/Effects/Actors/Attachments/Mounts/Objects jeweils **0**; `WaterRenderers=0`, `ModernRenderers=0`.
- Für vorbereitete Grasplatzierungen gibt es im normalen Shutdownlog keinen separaten Zähler. Ihre Freigabe ist in den unveränderten H2-Gates/Map-Destroy-Probes belegt; eine neue normale A1/B1-Wechselfolge mit separat beobachteten Placement-Zählern wird hier nicht behauptet.
- `renderer-failure.log` enthält lediglich `Renderer failure diagnostics enabled`, keinen Rendererfehler. Das erste `syserr.txt` ist nicht leer: einmal `invalid idx 0` sowie Damage-Effect-Diagnosezeilen. Diese werden nicht als Diligentfehler gezählt; ein vollständig fehlerfreies Python-/Spiellog wird nicht behauptet.

## Grenzen und Abschlussbedingung

Der erste Start aus der eingeschränkten Shell scheiterte an `0xc0000142`; der autorisierte Desktopstart funktionierte. Ein vorbestehender Prozess PID 16452 hat kein Hauptfenster und keinen auslesbaren Pfad in dieser Umgebung. `CloseMainWindow()` gab false zurück; keine erzwungene Beendigung und keine aggressive Systemaktion. Dieser Prozess zählt nicht zur Abnahme.

Der zweite Originallauf (PID 39184, 13:23:28 bis 13:29:23, Wien) erreichte nach Nutzeranmeldung ebenfalls C1 und endete mit Exit 0. Alle erfassten Diligent-/Fallback-/Shutdown-Zähler sind erneut 0. 9.125 Modern-Frames, 83.726 Water-Draws, 8.047 SSR-Frames, 72.320 Shimmer-Draws, 584.347 GPU-Actor-Frames und 916 native GR2-Reads belegen aktive Produktionspfade. C1 wurde mit 20/20 Tiles und 539.411 Grasplatzierungen in 69,5831 ms vorbereitet. `smoke-2/` enthält die vollständigen Belege.

Die Computer-Use-Fensterbilder konnten gelesen werden; Escape und Optionsklick bewirkten auch nach erneuter Beobachtung keine Menüöffnung. Der Client fordert laut unverändertem Buildmanifest Administratorrechte. Es wurden weder Rechte noch Manifest verändert und keine alternative Eingabeinjektion eingesetzt. Deshalb erfolgte die interaktive Restprüfung manuell durch den Nutzer, der bestätigte: **„Alles geprüft und fehlerfrei; Client normal geschlossen“**. Damit ist seine Sicht-/Bedienabnahme dokumentiert. Allerdings enthalten beide erfassten Originalläufe ausschließlich C1 und keinen weiteren Map-Ladevorgang. Die konkrete A1/B1-Wechselfolge wird bis zur Auflösung dieser Evidenzabweichung nicht als bewiesen geführt.

Es wurden keine Zugangsdaten angefordert oder Authentifizierung automatisiert. Die bestehende technische Release-/Debug-/LP64-/Classic-Abnahme (72/72, 72/72, 43/43, 12/12 bytegleich) bleibt unverändert; keine neue Golden-Erzeugung, kein unnötiger Neubuild und keine neue Featureentwicklung.

**H2-X FINAL / Production FINAL = NO-GO, bis die fehlende Originalclient-Mapwechsel-Evidenz geklärt ist.** Die Nutzer-Sichtabnahme ist bestätigt und die belegte Debug-Deployment-Lücke geschlossen. Source-/Runtime-Commits werden ausschließlich nach vollständig erreichtem FINAL GO erstellt. Kein Push, keine Folgephase.

## Nachweise

Alle lokalen Rohbelege liegen im Source-Repository unter `build-h2x/production-final-20260916/`: `deployment-audit.json`, `zero-audit-build.json`, `root-pack-source.tsv`, `debug-deployment.json`, `normal-launch.json`, `normal-exit.json`, `normal-launch-2.json`, `normal-exit-2.json`, `smoke-1/`, `smoke-2/`, `original-client-result.json`, `01-original-ingame.png` und die gesicherten vorherigen Dateien unter `before-runtime/`. Die frischen Root-Logs wurden nach hashgeprüfter Archivierung auf den exakt vorgefundenen Inhalt zurückgesetzt; die vier ausschließlich durch diesen Audit erzeugten neuen Root-Diagnoselogs wurden nach Hashvergleich entfernt. Die Originalordner-Logs sind daher nicht der Verweis auf die abgeschlossenen Auditläufe; dafür sind die beiden gesicherten Smoke-Verzeichnisse maßgeblich. Die Exe-/Paketdateien und Rohbelege sind ignorierte lokale Artefakte; die Dokumentation ersetzt kein Binary-Repository oder veröffentlichtes Releasepaket.

## P0-L FINAL Production Deployment – 17.09.2026

**PRODUCTION DEPLOYMENT = GO** für das angeforderte kurze Release-/Offline-Gate. Installiert am 17.09.2026 um 18:57 Uhr (Wien) in `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client`. Ausschließlich Deployment und Smoke; keine neue Optimierung, keine Produktcodeänderung, kein P1, kein Commit, kein Push.

| Identität | Verifizierter Stand |
| --- | --- |
| Source Branch / HEAD | `codex/g56-hdr-atmosphere` / `80f77391fe28e533c20e1e686525c7f444c6c2ca` |
| Python-/Runtime-Branch / HEAD | `codex/g56-hdr-colors` / `fabe77373bd561fb2f512449915ad5ab3c1fef62` |
| Release-Build | Frischer MSBuild-Rebuild von `UserInterface` und Abhängigkeiten, Release/x64, Exit 0; installierter Hash entspricht exakt dem neuen Buildoutput |
| Tatsächliche Startdatei / Arbeitsverzeichnis | `m2dev-client/Metin2_Release.exe` / normaler Clientordner; kein Testclient gestartet |
| Ersetzte Runtime-Dateien | `Metin2_Release.exe`, `pack/root.pck` |
| Python-Paketvergleich | 342 Einträge, genau `playersettingmodule.py` geändert, 0 hinzugefügt; neues Paket 342/342 bytegleich mit `assets/root` auf `fabe7737` |

Der freigegebene Quellstand enthält persistenten Shader-Bytecodecache, GR2-Decoder-, Area- und Animationsparallelismus, First-Use-Closure und optimierte Runtime-Key-Erzeugung zusammen mit G8/H2/Diligent. Der Neubau meldete lediglich die bestehenden Python/zlib-PDB-Linkerwarnungen. Der erste eingeschränkte Buildversuch scheiterte vor dem Build am Windows-SDK-Zugriff; der vollständige Neubau in der installierten VS-x64-Umgebung bestand.

### Backup und Dateiintegrität

Backup außerhalb des aktiven Runtimepfads: `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client-src\build-p0l-final-production\backup\`. Gesichert sind beide ersetzten Dateien sowie die kleinen Runtime-Dateien und Konfigurationen/Logs, die der Smoke schreiben kann; keine vollständige Clientsicherung.

| Datei | SHA256 |
| --- | --- |
| Alte Release-EXE | `9039416138E0DBBC61E94B6A0CE7DEA72F401024E5E1FA5943A12D5A11D8490F` |
| Backup der alten Release-EXE | `9039416138E0DBBC61E94B6A0CE7DEA72F401024E5E1FA5943A12D5A11D8490F` |
| Neue produktive Release-EXE | `7D4582444DC7DF7D18099D62E2DF0222DA1642D00423A322A3C10BAA24EB8F19` |
| Altes Root-Paket / Backup | `0C1C6F47E6DCE89D912363882789D76B3CFE1395CAD0290E2B59A7D434092994` |
| Neues produktives Root-Paket | `6A6D2017373876FBEBF4774A90AFB1712C0FD78D33A0B83C083CA875185B4CF3` |

549 Dateien vor/nach dem Deployment gehasht: genau zwei erwartete Runtime-Ersetzungen und **547 unveränderte geschützte Dateien**, darunter andere Pakete, Debug-EXE, Root-Assetquellen, Konfigurationen und vorherige Logs. Benutzereinstellungen wurden nach jedem Lauf bytegenau wiederhergestellt. Neue Smoke-Logs wurden hashgeprüft im Evidenzordner archiviert und aus dem aktiven Client entfernt. Vorhandene Cacheinhalte blieben unberührt; keine Screenshots erzeugt.

### Originalclient-Smoke und vollständige Production-Vorbereitung

Zwei neue Originalclient-Prozesse, PID **45616** (leerer isolierter Cache) und **42808** (derselbe gefüllte Cache), jeweils Exit **0** und `ShutdownClean`. Pro Lauf: **A1 vollständig laden → Player/Mob Idle, Walk, Run, Attack, Damage, Death jeweils dreimal → B1 vollständig laden → A1 erneut → normaler Exit**. Die 36 Motion-Prüfungen liegen vor B1; damit wird der erste Einsatz unmittelbar nach dem ersten A1-Load geprüft.

Für diesen autorisierten Offline-Smoke wurde vorübergehend ausschließlich `prototype.py` im installierten Root-Paket durch den bestehenden Loading-Probe ersetzt. Paketvergleich gegen das neue Produktionspaket: 342 Einträge, nur dieser Starteinstieg abweichend. Der Probe ist mit `LOAD_PREWARM = True` aktiviert, ruft in einem aktiven GPU-Frame **`chrmgr.PrewarmVisibleActors(True)` vor der ersten Weltpräsentation** auf und verwendet die installierte `playersettingmodule.py`-Batchgrenze. Dies ist derselbe vollständige native Funktionskörper wie `PythonNetworkStream::PrepareGamePhase`, einschließlich lokaler Player-Ressourcen und Damage-/Death-Auswahl. Die Motion-Prüfungen wurden für die verlangte Reihenfolge unmittelbar hinter A1 gelegt; Screenshot-Ausgaben deaktiviert. Nach jedem Prozess ist das normale Produktionspaket mit unverändertem Netzwerk-Starteinstieg wieder installiert und hashgeprüft.

A1 bestätigt **646 Animations-Dateijobs**, maximal **4 Worker**, vollständigen Production-Prewarm **706,8872 ms**, `NativePrewarmFailures=0` und `NativePrewarmLimited=0`. Keine feinen Runtime-Preparation-Profilmarker aktiv. Kein Netzwerklogin und keine neue manuelle Sichtabnahme; die Offline-Abdeckung war für dieses Gate ausdrücklich zulässig.

### Shadercache und Ladezeit-Sanity

Isolierter Cache: `m2dev-client-src/build-p0l-final-production/shader-cache`, vor dem ersten Start leer. Der erste Prozess erzeugte **73** gültige Einträge. Nach vollständigem Exit verwendete der zweite Prozess **125/125** bekannte Shader-Anfragen aus dem Cache: 48/48 beim Setup und 77/77 bei A1; **0 Misses, 0 Runtime-Compiles, 0 invalid/write-failure**. Alle 73 Cachedateien blieben über den Neustart SHA256-identisch; DXBC-Inhalte entsprechen den frisch kompilierten Ergebnissen. Der bestehende Standardcache unter `%LOCALAPPDATA%` wurde nicht geleert oder überschrieben.

| Sanity im neuen Prozess mit gefülltem Cache | Zeit |
| --- | ---: |
| A1 bis stable-present, vollständiger Prewarm enthalten | **1968,0171 ms** |
| A1 erste Weltpräsentation nach Preparation | 1931,2796 ms |
| B1 | 262,7116 ms |
| A1 nach Rückkehr | 163,4102 ms |

Der einmalige Empty-Cache-A1-Lauf brauchte 3569,1026 ms einschließlich 55 Shaderkompilierungen in A1; das ist kein Warm-Cache-Regressionswert. Der neue Prozess mit gefülltem Cache liegt bei **1,968 s**, plausibel zum freigegebenen Stand von rund 2,0 s. Keine Benchmarkserie und kein geleerter Betriebssystem-Dateicache.

### First Use, Zero Legacy und Fast Gate

Maximaler nativer Motion-Aufruf innerhalb des jeweils ersten Beobachtungsfensters im Warm-Cache-Prozess:

| Actor | Attack | Damage | Death |
| --- | ---: | ---: | ---: |
| Player | 0,0057 ms | 0,0103 ms | 0,0057 ms |
| Mob | 0,0061 ms | 0,0057 ms | 0,0062 ms |

Über alle 72 Motion-Fenster beider Prozesse maximal **0,0117 ms**; **0 neue Runtime-Keys, 0 Clip-Misses, 0 Key-Allokationsanforderungen, 0 späte GR2-Parses**. Keine erneuten 50–80-ms-Runtime-Key-Stalls. Walk-/Run-/Kampf-/Reaktionsclips im nativen Runtimepfad ausgeführt; keine visuelle Behauptung aus ungemessener Handbedienung.

**Zero Legacy PASS:** Importprüfung der tatsächlich installierten Release-EXE ohne D3D9-/D3DX9-, Granny-/granny2.dll- oder SpeedTree-Abhängigkeit; einschlägige SDK-Runtime-Marker ebenfalls 0. Native Logs bestätigen `GrannyFileReads=0` bei aktivem eigenem GR2-Pfad.

**Fast Gate PASS in beiden Prozessen:** A1/B1/A1, Animationen, persistenter Cache und sauberer Exit. `DiligentErrors=0`, `DiligentFatals=0`, `GPUFallbacks=0`, `AllCPUDeformationCalls=0`, `AllCPUDeformationVertices=0`; sämtliche vom vorhandenen Fast-Gate geprüften Shutdown-Ressourcen 0, einschließlich Source-/Skin-/Vegetation-/Asset-/GR2-/Animation-/Prototype-Ressourcen sowie Modern/Water und Terrain-/Objekt-/Mount-Ressourcen. Python-Fehlerlogs der beiden Läufe leer.

### Git und lokale Nachweise

Runtime-Git zum Abschluss: ausschließlich `docs/production-milestone-deployment.md` geändert; die beiden schon vorher unversionierten Dateien `docs/p0l-map-loading-deployment.json` und `docs/p0l2-shader-loading-deployment.json` bleiben unverändert. Die ersetzte EXE und das Root-Paket sind ignorierte Runtime-Ausgaben. Keine weiteren Script-/Configänderungen. Logs archiviert, vorhandene Logs wiederhergestellt; Shadercache, Backups und Smoke-/Buildartefakte liegen im ignorierten Source-Buildordner. Nichts gestagt, kein Commit, kein Push. Source-Git unverändert bis auf die bereits vorgefundene unversionierte `docs/performance/p0l3-shader-pso-breakdown.md`.

Lokale Evidenz unter `m2dev-client-src/build-p0l-final-production/`: `build-release.log`, `deployment.json`, `backup-manifest.json`, `protected-before.json`, `protected-after.json`, Paketvergleichs-TSVs, `zero-legacy.json`, `shader-cache-check.json`, `result.json`; je `empty/` und `warm/` Launch/Exit, native Traces, Ressourcen-/Lifecycle-Logs, `fast-gate.json` und `first-use-analysis.json`. Bestehende Prüfer aus `tests/Loading` wiederverwendet; keine vollständige Testsuite oder Visual-Galerie ausgeführt.

**Client neu starten. STOP nach diesem Deployment.**

## P2 FINAL Production Deployment – 17.09.2026

**P2 PRODUCTION = GO. P2 deployed. Source Commit: `4b2477d`.** Frischer Release-Build, EXE-Deployment und kurzes Originalclient-Gate abgeschlossen. Keine weitere Optimierung, kein P3, keine Änderung an VSync/Present/FPS-Limiter, kein Commit und kein Push.

### Identität, Backup und Deployment

| Punkt | Verifizierter Stand |
| --- | --- |
| Source | `m2dev-client-src`, Branch `feature/p2-runtime-performance`, HEAD `4b2477db3e2653279a49ba86f0684b987e05d8b7`, Worktree vor/nach Deployment sauber |
| Runtime | Normaler `m2dev-client`, Branch `main`, HEAD `d54637a4b323b9d40f0e200951c40d4d226a2cfc` |
| Finaler Build | Frischer MSBuild-Rebuild von `UserInterface` und Abhängigkeiten, Release/x64, Exit 0; bestehende Python/zlib-PDB-Linkerwarnungen |
| Dauerhaft ersetzt | Ausschließlich `Metin2_Release.exe`; installierter SHA256 identisch mit frischem Buildoutput |
| Deployment-Zeit | 2026-09-17T20:56:13.4650956+02:00 |
| Alte EXE / verifiziertes Backup SHA256 | `7D4582444DC7DF7D18099D62E2DF0222DA1642D00423A322A3C10BAA24EB8F19` |
| Neue EXE SHA256 | `DFC1165FC0D3AB44D8E94DC8CAB63EAF1D0BB2F47895C38406488B26B12A3E9D` |
| Unverändertes Produktions-Root-Paket SHA256 | `6A6D2017373876FBEBF4774A90AFB1712C0FD78D33A0B83C083CA875185B4CF3` |

EXE-Backup: `m2dev-client-src/build-p2-final-production/backup/Metin2_Release.exe`. Zusätzlich wurde nur das tatsächlich vorübergehend ersetzte `pack/root.pck` gesichert. Die drei durch den Smoke überschriebenen bisherigen Logs (`renderer-startup.log`, `vegetation-runtime.log`, `log/syserr.txt`) liegen unter `backup/smoke-state/` und wurden danach bytegenau wiederhergestellt. Keine vollständige Clientkopie. Von 549 geschützten Dateien ist ausschließlich die Release-EXE dauerhaft geändert; **548 unverändert**, einschließlich Debug-EXE, Paketen, Assetquellen, Einstellungen und bisherigen Logs.

Die freigegebene EXE enthält die P2-Mesh-/Shadow-Bindungswiederverwendung, native Dust-Texture-Lifetime und gepufferte optionale Effect-Diagnose sowie den bestehenden P0-L-/Shadercache-/GR2-/Animation-/Production-Prewarm-Stand. Der native Standard bleibt `m_iFPS = 60`; der P2-Commit verändert keine Pacing-Datei. `app.RuntimePerf` ist in der produktiven EXE nicht vorhanden; keine uncapped-Konfiguration oder Profiling-Binary übernommen. Die kurzen nativen FPS-Zähler meldeten in allen Phasen beider Läufe **61 Render-/Update-FPS** im bestehenden nominellen 60-FPS-Pfad. Uncapped-Present-Tails wurden nicht bewertet oder bearbeitet.

### Originalclient-Smoke und Sichtprüfung

Tatsächlich gestartete Datei: `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client\Metin2_Release.exe`, Arbeitsverzeichnis derselbe Originalordner. Kein Testclient gestartet. Zwei kurze Prozesse: **PID 22492**, 118.11 s, und sichtbare Wiederholung **PID 42796**, 117.68 s; jeweils Exit **0** und `ShutdownClean`.

In beiden Läufen: **A1 Idle → Laufen → volle Kameradrehung → Kampf/Effekte → dieselbe 25-s-Traversal-Strecke zweimal → B1 → A1 zurück → sauberer Exit**. Vollständiger nativer `chrmgr.PrewarmVisibleActors(True)` im aktiven GPU-Frame vor den Beobachtungsphasen; `NativePrewarmFailures=0`, `NativePrewarmLimited=0`. Bestehende Grafikqualität und View Distance beibehalten. Vorhandener Shadercache in einem isolierten Evidenzverzeichnis wiederverwendet; der Benutzer-Cache unverändert.

Für den netzwerkfreien Smoke wurde ausschließlich `prototype.py` im installierten Root-Paket vorübergehend ersetzt. Vergleich: **342 Einträge, genau 1 Änderung, 0 neue Einträge**. Die 341 anderen Einträge entsprechen bytegenau dem vorgefundenen Produktionspaket. Die losen Runtime-Assetquellen haben 121 bereits bestehende reine Zeilenendenabweichungen gegenüber diesem Paket; deshalb wurde der zuvor gesicherte, vollständig gegen das installierte Paket geprüfte Inhalt als Smoke-Basis verwendet. Keine dieser Abweichungen wurde deployed oder korrigiert. Nach jedem Exit normales Netzwerk-Startpaket bytegenau zurückgespielt und SHA256 geprüft. Kein Netzwerklogin erforderlich oder ausgeführt.

Die erste Sichtprüfung konnte der Nutzer nicht beobachten. Danach wurde der zweite Lauf ausdrücklich sichtbar gestartet. Nutzerbestätigung nach diesem Lauf: **„Alles vollständig und unauffällig; Lauf beendet“**. Damit sind vollständige Meshes/Schatten/Materialien/Effekte, ruhige Vegetation und keine auffälligen neuen sichtbaren Ruckler für diesen kurzen Ablauf bestätigt. Zusätzlich drei native Einzelbilder des ersten Laufs auf sichtbare Inhalte geprüft; keine Visual-Galerie oder große Testsuite.

### P2-Sanity, World Stability und Fast Gate

| Prüfung | Ergebnis |
| --- | --- |
| Dust Resources | **PASS:** Dust im nativen Effect-Pfad aktiv. Während der wiederholten 25-s-Strecke jeweils **0 Pack-Reads, 0 CreateTexture, 0 CreateBuffer** insgesamt, damit auch keine erneuten Dust-Reads/-Creations. Je rund 1.516 präsentierte Frames; aktive Mesh-/Vegetation-Requests belegen das Beobachtungsfenster. |
| Effect Burst / optionale Diagnose | **PASS:** In allen Gameplay-Phasen beider Prozesse existiert noch keine `effect-renderer.log`; erst beim sauberen Exit werden jeweils 34 deduplizierte Diagnosezeilen geschrieben. Kampf-, Dust- und Wasserfalleffekte aktiv, keine Effect-ERROR-Zeile. Der beanstandete synchrone Diagnose-Schreib-/Flush-Pfad belastet diese Gameplay-Frames nicht; keine neue Zeitmess-/Optimierungsserie. |
| Static / Shadow Resources | **PASS:** Sichtprüfung bestätigt; erster Lauf 1.069.864 Mesh-Draws und 2.476.647 Shadow-Draws, keine Binding-/Rendererfehler. |
| Sektoren / Terrain / World | **PASS:** Innerhalb sämtlicher Bewegungsphasen keine Terrain-/Area-Loads/-Unloads, keine Terrain-Neuzuweisung und keine neu erstellten Bäume. Auf der Wiederholungsstrecke auch keine Buffer-/Texturerstellung; kein Hinweis auf Terrain-Patch-/World-Rebuild. Keine neue feine Patch-Instrumentierung eingebaut. |
| Instance Buffer / Vegetation | Erste Traversal-Erschließung 6 Instance-Buffer-Erstellungen; wiederholte Strecke **0**, dazu **0 neue Bäume und 0 LOD-Wechsel**. Kein wiederholter Aufbau; Sichtprüfung bestätigt fehlendes neues Flattern. |
| Fast Gate | **PASS in beiden Originalläufen:** Release, A1/B1/A1, Laufstrecke, Effekte, Exit 0, `ShutdownClean`, leeres frisches Python-Fehlerlog. |
| Diligent / GPU / CPU | `DiligentErrors=0`, `DiligentFatals=0`, `GPUFallbacks=0`, `AllCPUDeformationCalls=0`, `AllCPUDeformationVertices=0`. |
| Shutdown | Alle vorhandenen Fast-Gate-Ressourcen **0**: Source, Skin, Paletten, Collision, Vegetation, Assets, GR2, Animation, Prototypes, Modern/Water sowie Terrain-/Objekt-/Mount-Ressourcen. |
| Zero Legacy | **PASS:** Imports der tatsächlich installierten EXE ohne D3D9/D3DX9, Granny/granny2.dll und SpeedTree; einschlägige SDK-Marker 0. Native Logs `GrannyFileReads=0` bei aktivem eigenem GR2-/Vegetationspfad. Nur kurze Sanity, kein erneuter Vollaudit. |

Für die beiden Traversal-Fenster wurde ausschließlich der vorhandene optionale `MapLoadTrace` mit bereits vorhandenen Zählern verwendet. Erste Sichtbarkeits-/Ressourcennutzung ist von der unveränderten Wiederholung getrennt; keine Behauptung, dass beim allerersten Besuch keinerlei Ressourcen entstehen.

### Git, Nachweise und STOP

Runtime-Abschlussstatus: ausschließlich ` M docs/production-milestone-deployment.md`; nichts gestagt. Source weiterhin sauber auf `4b2477d`. Keine Logs, Caches, Backups, Screenshots, Traces, Debug-Dateien oder Benchmarkdaten deployed/gestagt. Frische Smoke-Dateien wurden hashgeprüft außerhalb des aktiven Clients archiviert und aus dem Runtimeordner entfernt; frühere Logs und Konfigurationen sind wiederhergestellt.

Lokale Nachweise im ignorierten Source-Verzeichnis `build-p2-final-production/`: `build-release.log`, `deployment.json`, `backup-manifest.json`, `protected-before.json`, `normal-staging-source.tsv`, `smoke-pack-diff.tsv`, `production-imports.txt`, `zero-legacy.json`, `result-smoke.json`, `result.json`, `manual-acceptance.json`, `final-result.json`; unter `smoke/` und `visual/` jeweils Launch-/Exit-/Ressourcen-/Lifecycle-Nachweise und `fast-gate.json`. Keine Runtime-Commits, kein Push.

**Client neu starten. STOP nach P2 Production Deployment; kein P3 begonnen.**


## P3 FINAL — Production Deployment (2026-09-17)

**P3 PRODUCTION: GO.** Frisch gebaut und im normalen Originalclient installiert; kurzer Offline-Smoke und drei echte Persistenz-Neustarts bestanden. Keine neue Produktentwicklung, kein Commit, kein Push.

### Freigabestand und Deployment

| Punkt | Nachweis |
| --- | --- |
| Source | `186facd6ed31e032d636f351a1ab7dfb774f6851` (`186facd`), Branch `codex/p3-frame-pacing`, vor/nachher sauber |
| UI/Runtime | `f400975cbb9cfbd2613cc53e6eacd5e795422f3a` (`f400975c`), Branch `codex/p3-frame-pacing` |
| Ausgangsänderung | Ausschließlich die vorhandene Änderung dieser Deployment-Dokumentation; vollständiger vorgefundener Inhalt bytegenau erhalten und nur ergänzt |
| Release | Frischer vollständiger MSBuild-Rebuild von UserInterface einschließlich Abhängigkeiten, Release/x64, Exit 0; unverändertes freigegebenes Source-Tree. Bestehende Python/zlib-PDB-Linkerwarnungen. |
| Deployment | 2026-09-17T21:48:23.0587642+02:00; normale `m2dev-client/Metin2_Release.exe` und `pack/root.pck` ersetzt |
| Alte EXE / Backup SHA256 | `DFC1165FC0D3AB44D8E94DC8CAB63EAF1D0BB2F47895C38406488B26B12A3E9D` |
| Neue EXE / installierter Buildoutput SHA256 | `C32EC53DDFD9971398E6DA271F253E427BEA526E205B391789E0ACA7168B8A42` |
| Altes Root-Paket / Backup SHA256 | `6A6D2017373876FBEBF4774A90AFB1712C0FD78D33A0B83C083CA875185B4CF3` |
| Neues normales Root-Paket SHA256 | `B3B1AF29EAC53A8FD3C84A15D8D319963B15B80D69C75EBF5A00D932882184AF` |

Das Root-Paket enthält weiterhin **342 Einträge**. Genau **2 Einträge geändert**, **0 hinzugefügt**: `uichat.py` und `uigraphicssettings.py` aus dem freigegebenen UI-Commit. Belegt durch zwei aufeinanderfolgende vollständige Einzeländerungsvergleiche und anschließenden vollständigen Pack-/Source-Vergleich. Die übrigen 340 Einträge bleiben bytegleich. Bestehende Zeilenendenabweichungen loser Assetquellen wurden nicht mit deployed. Die bereits freigegebenen losen UI-Dateien bleiben unverändert.

Minimale hashgeprüfte Sicherungen: `m2dev-client-src/build-p3-final-production/backup/Metin2_Release.exe`, `backup/pack/root.pck`, `backup/config/graphics.cfg` und die vorgefundene Dokumentation. Während des Smoke überschriebene frühere Logs zusätzlich unter `backup/smoke-state/`; anschließend bytegenau wiederhergestellt. **549 geschützte Runtime-Dateien geprüft: nur EXE und Root-Paket dauerhaft geändert, 547 unverändert**, einschließlich Debug-EXE, aller übrigen Pakete, Assetquellen, Benutzereinstellungen und früherer Logs. Die Dokumentation wird zusätzlich ausschließlich erweitert.

Die EXE enthält den bestehenden P0-L-/P2-Stand und P3. Keine besondere Profiling-Binary oder neue Instrumentierung gebaut: `app.RuntimePerf` fehlt; `AnimationStallAudit=0`, `LoadWarmupAudit=0`. Der freigegebene optionale `--frame-pacing-capture` bleibt deaktiviert, keine `frame-pacing.csv` erzeugt. Ausschließlich für diesen kurzen Smoke vorhandene Renderer-/MapLoadTrace-Diagnose eingeschaltet; der wiederhergestellte normale Start aktiviert sie nicht. Keine Testclient-/Debug-Binaries, Traces, Screenshots, Logs, Caches, temporären Configs oder Benchmarkdaten dauerhaft deployed.

### Originalclient, Menü, Live Apply und Persistenz

Gestartet wurde ausschließlich `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client\Metin2_Release.exe`, Arbeitsverzeichnis derselbe Originalordner; installierter SHA256 vor jeder Ausführung geprüft. Hauptlauf **PID 38808**, **79.04 s**, danach drei kurze neue Prozesse. Der Offline-Start ersetzt vorübergehend ausschließlich `prototype.py` gegenüber dem neuen normalen P3-Paket (**342 Einträge, 1 Änderung, 0 neue Einträge**). Nach jedem Lauf wird das neue normale Netzwerk-Startpaket hashgeprüft wiederhergestellt. Kein Netzwerklogin, keine Visual-Galerie, keine lange Testsuite.

Das tatsächliche `OptionDialog → GraphicsDialog` im installierten Client wurde geöffnet und über die nativen ComboBox-Ereignisse bedient. **FPS-Limit: 60 / 120 / Unbegrenzt**, separate **VSync: Aus / Ein**; vollständige Eintragslisten sowie genau je eine Beschriftung geprüft. Keine doppelten Optionen oder Debug-Bezeichnungen in diesen Listen. Livefolge **60/Aus → 120/Aus → Unbegrenzt/Aus → 60/Aus → 60/Ein → 60/Aus** im selben Prozess bestanden; vor jeder Beobachtung bestätigte der Renderer die neuen Werte. Keine Qualitäts-/Distanzänderung, keine komplette Renderer-Neuinitialisierung: ein Start-/Shutdown-Lebenszyklus, vorhandener Apply-Pfad aktualisiert die Runtime-Konfiguration.

| Persistenztest | Im vorherigen Prozess über das Grafikmenü gespeichert | Neuer Originalprozess bestätigt | Ergebnis |
| --- | --- | --- | --- |
| A | 120 / Aus | PID 23440, 4.02 s | PASS |
| B | 60 / Ein | PID 38008, 4.35 s | PASS |
| C | Unbegrenzt / Aus | PID 2204, 4.29 s | PASS |

Jeder Prozess las die Werte aus der bestehenden echten `config/graphics.cfg`; die Datei wurde zwischen diesen Neustarts nicht ersetzt. Abschließend ist die ursprüngliche Benutzereinstellung **bytegenau** wiederhergestellt (SHA256 `E8563E771A6DCC19E892B83729E3AB8A04A887185CF32E637BE807D3B4AE925F`). Da sie noch keine P3-Schlüssel enthält, gilt der vorgesehene Default **60 FPS / VSync Ein**; alle übrigen Präferenzen bleiben erhalten. Keine komplette Testkonfiguration übernommen.

### Kurzer Funktions- und Timing-Smoke

Alle sechs Kombinationen in A1 jeweils mit Idle, nativer Kameradrehung und echter `MoveToDestPosition`-Bewegung; zusätzlich native Attack-/Animations-/Effektfolgen bei 60, 120 und Unbegrenzt. Keine pro Frame simulierte Teleport-Bewegung. Die Werte sind kurze Render-Callback-Abstände und vorhandene native Zustandszähler, keine erneute vollständige P3-Benchmark- oder Present-Tail-Analyse.

| Kombination | Kurze beobachtete FPS über die Phasen | Ergebnis |
| --- | --- | --- |
| 60 / Aus | 60.00–60.01 | PASS |
| 60 / Ein | 60.00–60.01 | PASS |
| 120 / Aus | 120.00–120.04 | PASS |
| 120 / Ein | 120.00–120.02 | PASS |
| Unbegrenzt / Aus | 772.71–909.17 | PASS, eigener 60/120-Limiter aus |
| Unbegrenzt / Ein | 164.84–164.86 | PASS, Display-/Present-begrenzt |

VSync wird im unveränderten freigegebenen D3D11-Present-Pfad mit `PresentInterval(Off)=0`, `PresentInterval(On)=1` direkt an die SwapChain übergeben. Live-Wirkung durch den Wechsel von über 770 auf rund 165 FPS bestätigt. Aktuelles Display: RTX 5070 Ti, 2560×1440, WMI ganzzahlig 164 Hz, Treiber 32.0.16.1656. Aus garantiert weiterhin keine bestimmte Tearing-/DWM-/Treiberpolitik.

**10.664 Beobachtungsintervalle** in der sechsfachen Matrix, **0 über 20 ms**, Maximum **17.496 ms**; Lade-/Vorbereitungs- und Scriptwechselphasen sind getrennt. Simulation in diesen kurzen Fenstern **60.44–60.90 Updates/s**, maximale Spielzeit-/Wallclock-Abweichung **11.30 ms**. Native Laufgeschwindigkeit **431.109–431.453 Einheiten/Spielsekunde**, Kameradrehung **90.886–90.932 Grad/Spielsekunde**. Zwei vollständige Attackfolgen pro geprüftem FPS-Modus jeweils **1.006–1.007 s**, native Effekte aktiv (474/477/476 maximale Partikel). Kein vom Renderlimit abhängiger Gameplay-Speed festgestellt. Bestehende ungefähr 60.6-Hz-Simulation bleibt erhalten; keine zusätzliche Render-Interpolation.

**A1 → B1 → A1: PASS.** Nach A1-Laufen/Kampf/Effekten bei allen drei Limits: kurze native Bewegungswiederholung, Wechsel nach B1 und Bewegung, Rückkehr nach A1 und Bewegung, jeweils **120/Aus**, anschließend normaler sauberer Exit. Mapwechsel stammen aus diesem Originalclient-Prozess, nicht aus früheren privaten P3-Tests.

### P2, Shader/Animation und Fast Gate

| Prüfung | Frischer Originalclient-Nachweis |
| --- | --- |
| P2 Dust | Dust-Effekt aktiv. Kurze wiederholte native Laufstrecke: **301 Frames, 0 Pack-Reads, 0 CreateTexture, 0 CreateBuffer**; keine erneute Dust-Ladung. |
| P2 Effect-Diagnose | Während sämtlicher Gameplay-Fenster keine `effect-renderer.log`; erst nach Shutdown **33 deduplizierte Zeilen**, Kampf-/Dust-Effekte enthalten, kein Effect-ERROR. |
| P2 World Stability | In sämtlichen Beobachtungsfenstern 0 Terrain-/Area-Loads/-Unloads, 0 Terrain-Neuzuweisungen, 0 neue Bäume; Wiederholungsstrecke zusätzlich 0 neue Instance-Buffer. Kein wiederholter Sektor-/World-Aufbau in den vorhandenen Zählern. |
| Shadercache | Bestehenden warmen Cache mit 74 Dateien im isolierten Evidenzordner verwendet; **126 Anfragen, 126 Hits, 0 Misses, 0 Runtime-Compiles, 0 Invalid-/Write-Failure-Ereignisse**. Benutzer-Cache nicht verändert. |
| Animation Prewarm | `GR2Prewarm=1`, vor sichtbarer Beobachtung nativer `PrewarmVisibleActors(True)` im aktiven GPU-Frame; **1.364 Requests**, **0 Failures**, **0 Limited**. |
| Attack/Damage/Death First Use | Bei 120/Aus jeweils 0 neue Runtime-Key-Bytes, 0 Key-Allokationen, 0 Clip-Misses, 0 späte GR2-Parses. Native Motion-Maxima **0.0087 / 0.0100 / 0.0108 ms**; keine beobachteten First-Use-Stalls. |
| Fast Gate | **PASS in allen vier vollständigen Prozessen:** Exit 0, `ShutdownClean`, frische Python-Fehlerlogs leer. |
| Diligent / GPU / CPU | **Diligent ERROR/FATAL=0, GPU fallback=0, CPU deformation calls/vertices=0.** |
| Shutdown-Ressourcen | Sämtliche erfassten Source-/Skin-/Paletten-/Collision-/Vegetation-/Asset-/GR2-/Animation-/Prototype-/Modern-/Water-/Terrain-/Objekt-/Mount-Ressourcen **0**. |
| Zero Legacy | **PASS:** Imports der installierten EXE ohne D3D9/D3DX, Granny/granny2.dll oder SpeedTree; bekannte SDK-Marker 0. Startup: eigener GR2-Reader, AnimationRuntime, GPU-Skinning und ZiiNAN-Vegetation; `GrannyFileReads=0`. |

Die Auswertung ist eine automatisierte kurze Abnahme im normalen Originalclient; keine neue manuelle Sichtfreigabe oder Netzwerkprüfung behauptet. Ein erster 4-s-Prüfversuch endete wegen einer Script-Annahme über ein bereits automatisch geschlossenes Tracefenster; separat unter `attempt-1-trace-already-closed/` archiviert. Nur das temporäre Prüfscript wurde korrigiert, kein Produktcode oder Build geändert. Danach vier vollständige Läufe PASS.

### Abschluss und Nachweise

Runtime-Gitstatus weiterhin ausschließlich ` M docs/production-milestone-deployment.md`, nichts gestagt. Source sauber auf `186facd`; Runtime-HEAD unverändert `f400975c`. Kein Commit, kein Push. Temporäre Smoke-Dateien außerhalb des aktiven Clients hashgeprüft archiviert; normales P3-Startpaket und originale Konfiguration/Logs wiederhergestellt. Kein Clientprozess läuft weiter.

Lokale Nachweise unter `m2dev-client-src/build-p3-final-production/`: `build-release.log`, `build-result.json`, `deployment.json`, `backup-manifest.json`, `protected-before.json`, Packvergleichs-TSVs, `production-imports.txt`, `zero-legacy.json`, `result.json`, `display.json`, finale Git-/Integritätsnachweise. In `smoke/`, `restart-a/`, `restart-b/`, `restart-c/`: Launch-/Exit-/Konfigurations-/Lebenszyklus-/Ressourcenbelege, `p3-smoke.jsonl`, `fast-gate.json`. Sämtliche Prüfartefakte bleiben im ignorierten Source-Buildordner.

**Client neu starten. STOP nach P3 Production Deployment. Keine Interpolation, UI/Fonts 2.0, World-Editor-, Vulkan- oder weitere Performancearbeit begonnen.**
