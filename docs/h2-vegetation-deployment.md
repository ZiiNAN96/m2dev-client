> Aktueller Textur-/Release-Stand: [Alle Bodentexturen wieder original; flächiges 3D-Gras abgeschaltet](terrain-original-restoration.md). Die unten genannten EXE-Hashes und Gras-Erzeugung beschreiben den früheren H2-Stand; dessen übrige Abnahmegrenzen bleiben davon unberührt.

# H2-X: Übernahme in den normalen Spielclient

## Ergänzung: H2-X-FINAL-Audit vom 16.09.2026

Der [Production-Milestone-Audit](production-milestone-deployment.md) ergänzt den untenstehenden ursprünglichen Übernahmebericht. Release-EXE, Root-Paket und sämtliche 342 Root-Quellen wurden erneut abgeglichen und stimmen unverändert. Eine zusätzliche reale Deployment-Lücke wurde geschlossen: Die alte, noch von D3D9 abhängige `Metin2_Debug.exe` wurde am 16.09.2026 um 13:23:22 nach hashgeprüfter Sicherung durch den bereits freigegebenen H2-Debug-Build ersetzt. Neuer SHA256: `7e969342228a6428bfa2cdb65299d3429a813c1ee565b3c4dd34ed28731e0cff`. Die frühere Aussage „Debug unverändert“ gilt für das ursprüngliche Deployment um 12:43 Uhr, nicht für diese Ergänzung.

Ein frischer Start der normalen `Metin2_Release.exe` aus diesem Originalordner erreichte echten Login/Character Select/C1-Ingame und endete mit Exit 0. C1: 20/20 Kartenteile, 539.411 beim Laden vorbereitete Grasplatzierungen. Diligent ERROR/FATAL, CPU-Deformation, GPU-Fallbacks und alle erfassten Shutdown-Ressourcen: 0. Der Bild-/Logbeleg stammt vom Originalclient, nicht vom Testclient.

Ein zweiter Originallauf endete ebenfalls mit Exit 0 und allen erfassten Nullzählern 0. Der Nutzer bestätigte die manuelle Restprüfung als fehlerfrei und den normalen Exit. Allerdings enthalten beide erfassten Läufe ausschließlich C1; die konkrete A1/B1-Wechselfolge bleibt bis zur Klärung dieser Abweichung offen. **FINAL GO noch offen; kein Commit/Push.** Neue Belege und die alte Debug-EXE sind im Source-Repository unter `build-h2x/production-final-20260916/` gesichert. Vorhandene Benutzer-Grafikwerte wurden separat bewahrt; die von diesem Audit veränderten Root-Logs wurden nach hashgeprüfter Archivierung auf ihren exakten vorherigen Inhalt zurückgesetzt.

## Ursprüngliche Übernahme um 12:43 Uhr

Am 16.09.2026 um 12:43 Uhr (Wien) auf Nutzerauftrag lokal übernommen. Ziel: `C:\Users\ZiiNAN\Documents\GitHub\m2dev-client`. Die Änderung ist ab dem nächsten Start von `Metin2_Release.exe` aktiv; bereits laufende Clients übernehmen sie nicht automatisch.

## Verhalten und Umfang

Gras wird vollständig während des Kartenladens vorbereitet, einschließlich entfernter Kartenteile. Beim Vorbeilaufen werden keine Grasplatzierungen nacherzeugt. Entfernung, Ausblendung und Qualitätsstufe bestimmen weiterhin, welches vorbereitete Gras gezeichnet wird. Das hinzugefügte `config/graphics.cfg` aktiviert Modern / High; vorher war keine solche Einstellungsdatei vorhanden.

- `Metin2_Release.exe`: exakt die nach der Gras-Korrektur geprüfte Release-Datei.
- `assets/root/vegetation/`: Registry und SDK-freies Vegetationspaket mit 118 Legacy-Zuordnungen sowie den H2-Demoassets (249 Dateien).
- `assets/root/ymir work/vegetation/modern/`: sechs DDS-Texturen unter den vom Material erwarteten virtuellen Pfaden.
- `pack/root.pck`: aus diesen Quellen neu gepackt, insgesamt 342 Einträge. Dadurch bleiben die Assets auch beim regulären erneuten Packen erhalten. Kein separates loses Vegetationsverzeichnis erforderlich.

Alle 87 vorher vorhandenen Root-Quelldateien bleiben bytegleich. Gegenüber dem alten gepackten Root wurde lediglich das bereits vorhandene Grafikmenü `uisystemoption.py` aktualisiert und das vorhandene Modul `uigraphicssettings.py` zusätzlich eingepackt. Diese Menüquellen waren bereits Bestandteil des geprüften H2-Testclients; keine neue Menüimplementierung in dieser Übernahme.

`Metin2_Debug.exe`, alle anderen Pakete einschließlich `Tree.pck` und alle vorher vorhandenen Konfigurationsdateien sind per SHA256 unverändert. Die beiden ersetzten Dateien wurden gesichert und atomar ausgetauscht.

## Prüfung

- SHA256 der installierten EXE: `959d03d5ff6e560a2043e300688811852ff56784d14236aea541a0ab003964cd`.
- SHA256 des installierten Root-Pakets: `0c1c6f47e6dce89d912363882789d76b3cfe1395cad0290e2b59a7d434092994`.
- Paketprüfung: 342/342 entpackte Einträge stimmen mit den installierten Quelldateien überein; alle alten Paketeinträge bleiben vorhanden.
- Gezielter nativer Pakettest: PASS, drei B1-Ansichten, 1.138 Frames, 26,36 Sekunden, Exit 0. Der Testclient verwendete ein eigenes Startskript und die übernommenen Root-Quellen; sein loses Vegetationsverzeichnis war deaktiviert.
- Vor dem ersten Weltbild: 578.476 Grasplatzierungen, 20/20 Kartenteile, Vorbereitung 77,84 ms. Entfernter Kartenteil und Rückkehr behalten dieselben Platzierungen und denselben Vorbereitungsvorgang. Nach Map-Destroy: null Platzierungen.
- Vegetationsfehler, Diligent-Fehler, CPU-Deformation, GPU-Fallbacks und geprüfte Shutdown-Ressourcen: jeweils null; Python-Fehlerprotokoll leer.

Die vollständigen Release-/Debug-/LP64-/Classic-Gates stammen aus der unmittelbar vorherigen Prüfung desselben Client-Binaries und wurden für diese Paketübernahme nicht erneut ausgeführt. Kein Netzwerk-Login oder Relog getestet. Künstlerische Sichtabnahme und allgemeines Performance-GO bleiben getrennt.

## Nachweise und Sicherung

Im benachbarten Source-Repository liegen unter `build-h2x/deployment-20260916/` das Vorher-Inventar `before.json`, der Dateiplan `deployment.json`, der Übernahmebeleg `installed.json`, der Prüfabschluss `verification.json` und die Paketvergleiche `staged-pack-diff.tsv` / `installed-pack-source.tsv`. Die ursprüngliche EXE und `pack/root.pck` liegen unter `backup/`. Die drei nativen Aufnahmen und Protokolle liegen unter `build-h2x/runtime-deployment-check/`.

Für eine Rücknahme zuerst den Client schließen, anschließend die beiden gesicherten Dateien per Dateiaustausch zurückspielen und das neu hinzugefügte `config/graphics.cfg` entfernen, sofern es seither nicht bewusst verändert wurde. Die 255 hinzugefügten Asset-Quelldateien sind einzeln in `deployment.json` aufgeführt; sie müssen bei einer vollständigen Rücknahme ebenfalls entfernt werden, damit späteres Packen sie nicht wieder einführt. Vor einer Rücknahme etwaige nachfolgende Änderungen anhand der protokollierten Hashes prüfen.

Kein Commit, kein Push, keine Folgephase. Codeänderungen bleiben im Source-Repository; die neuen Assetquellen und diese Dokumentation liegen im normalen Client-Repository. Die EXE und das erzeugte Paket sind lokale, von Git ignorierte Laufzeitdateien.
