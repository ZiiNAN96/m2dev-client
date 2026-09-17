# Stabile Bäume im Originalclient

Stand: 17.09.2026. Der Nutzer hat die Darstellung mit fester höchster Baumstufe
visuell freigegeben und die Übernahme sowie Bereinigung des Originalclients
beauftragt. Release und Debug sind auf diesen Quellstand aktualisiert.

Modern-Bäume verwenden durchgehend dieselbe vollständige höchste 3D-Stufe.
Entfernungsabhängige Baum-Modellwechsel und deren Überblendung entfallen.
Sichtweite, Frustum-/Entfernungs-Culling, Wind, deckende Stämme und ausgeschnittene
Blätter bleiben erhalten. Der bereits geprüfte BUGFIX-X-Stand für Kartenresidenz
und Gelände ist enthalten. Classic behält seinen bisherigen Darstellungsweg.
Flächiges 3D-Gras bleibt abgeschaltet; Originaltexturen und Assetpakete bleiben
unverändert. Die persönlichen Grafikeinstellungen wurden nicht überschrieben.

## Installierte Dateien

| Datei | Bytes | SHA256 |
| --- | ---: | --- |
| `Metin2_Release.exe` | 31.106.048 | `6ed6c0047cbd7dd6f4a8deca35b3a35c72b7040e4a4580bbabfc798f4afda1ce` |
| `Metin2_Debug.exe` | 43.071.488 | `e58526a70c5ac538aeef77c71fe5f402d53bf814a6598b0c21fee155c709dd4b` |
| `pack/root.pck`, unverändert | 6.778.061 | `0c1c6f47e6dce89d912363882789d76b3cfe1395cad0290e2b59a7d434092994` |

Release ist bytegleich mit dem visuell freigegebenen separaten Testclient.
Debug wurde aus demselben unveränderten Quellstand frisch gebaut; seine sechs
gezielten Vegetationsprüfungen einschließlich GPU-Test bestanden in 5,57 Sekunden.
Die bestehenden Release-Prüfungen (6/6), GCC-Prüfungen (3/3) und der native
150-Sekunden-Lauf auf A1/Trent (8.988 Frames, keine Grafikfehler, geprüfte Ressourcen
beim Beenden null) bleiben dem exakt abgeglichenen Release-Quellstand zugeordnet.
Der kurze Vergleich ergab praktisch unveränderte GPU-Zeit: A1 0,649 → 0,636 ms,
Trent 0,599 → 0,595 ms. Das ist keine allgemeine Worst-Case-Leistungsgarantie.

Der tatsächliche Root-Pack stimmt in allen 342 Einträgen mit `assets/root`
überein. Es wurde kein Test-Startskript übernommen und kein Paket neu gepackt.
Die normale Netzwerkanmeldung des Originalclients bleibt bestehen. Die frühere
umfassende H2-Lifecycle-/Mapwechsel-Abnahme wird durch dieses Deployment nicht
nachträglich als vollständig bewiesen bezeichnet.

Startprüfung im tatsächlichen Originalordner bestanden: `Metin2_Release.exe`,
PID 40516, reagierendes `METIN2`-Fenster, freigegebener Binärhash. Der Start erfolgte
ohne Testargumente; `renderer-startup.log` bestätigt `VerboseDiagnostics=0` und
Diligent D3D11. Der Originalclient wurde für den Nutzer geöffnet gelassen.
Beleg: `evidence/original-start.json` im unten genannten Deploymentverzeichnis.

## Bereinigung und Sicherung

13 alte Laufzeit-/Diagnoseprotokolle mit insgesamt 1.292.245 Bytes wurden nach
Inventarisierung und verifiziertem Backup aus dem Originalordner entfernt.
Die neun bisher versionierten Root-Diagnoselogs werden nicht mehr versioniert;
neu erzeugte Root-Logs und der Diagnose-Benchmark werden künftig ignoriert.
Neue kleine Laufzeitlogs können beim normalen Clientstart erneut entstehen.

54.692 geschützte Dateien blieben unverändert: sämtliche Assetquellen, 91 Pakete,
Konfigurationen, Musik, Gilden-/Upload-Ressourcen und `config.exe`. Verglichen
wurden vollständige Dateimetadaten sowie SHA256 für Pakete, Root-Assetquellen,
Konfigurationen und die übrigen geschützten Laufzeitressourcen. Historisch benannte
`*_backup.gr2` und `.mse.bak` innerhalb der Assetquellen wurden als Content erhalten.

Backups liegen außerhalb des Originalclientordners unter:

`C:\Users\ZiiNAN\Documents\GitHub\m2dev-client-src\build-bugfix-x\fixed-detail\deployment-20260917\backup`

Dort sind die bisherigen beiden EXEs, Root-Pack, Einstellungen, Dokumentation,
Ignore-Datei und archivierten Logs erhalten. `inventory.json`,
`protected-files.json` und `result.json` im übergeordneten Deploymentverzeichnis
dokumentieren Dateigrößen, SHA256, Dateikennungen, Hardlinks und Ergebnis. Die EXEs
wurden durch neue Dateieinträge ersetzt, um eventuell vorhandene Hardlinks auf
frühere Versionen nicht mitzuschreiben.

**Client neu starten**, damit ein zuvor laufender Prozess die neue Version lädt.
Kein Commit und kein Push.
