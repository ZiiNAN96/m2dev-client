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
