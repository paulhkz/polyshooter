# Projekt: Polyshooter

**Python Version:** Python 3.14

## 1. Beschreibung der Spielfunktionen

Dieses Programm ist ein Hangman-artiges Spiel, um [Johnson-Körper](https://de.wikipedia.org/wiki/Johnson-K%C3%B6rper) zu erraten. Diese sind spezielle Polyeder. Eine tiefere Beschreibung sowie eine vollständige Liste befindet sich in dem hinterlegtem Link.

Die Geschichte hinter diesem Spiel ist, dass sich über der Erde ein Portal geöffnet hat und diese Körper herunterfallen, welche beim Einschlagen ein Krater hinterlassen. Es gibt einen Laser, welcher sich so kalibrieren kann, dass er den Polyeder vernichten kann. Dafür muss dieser aber den Aufbau des Körpers kennen, was der Spieler errät.

Diese Story wird dem Spieler anfangs angezeigt, welcher er mit 's' überspringen kann oder eben lesen kann. Danach fängt das Spiel an. Dabei gibt er einzelne oder eine Reihe von Buchstaben ein. Diese werden getestet, ob sie valide (alphabetisch) sind. Wenn nicht, werden sie ignoriert. Außerdem werden sie zusätzlich zu Kleinbuchstaben konvertiert.

Als nächstes wird geschaut, ob das zu erratende Wort diese(s) Buchstaben enthält. Wenn ja, werden alle Buchstaben im nächsten Zug aufgedeckt. Wenn nein, zeigt die Anzeige wie weit der Johnson-Körpern entfernt ist an, dass er näher kommt.

Nachdem alle Buchstaben aufgedeckt wurden, wird der Spieler gefragt, ob er nochmal spielen will. Der nächste Körper fällt jedoch in eine Richtung, sodass der Spieler nicht verpflichtet ist, weiter zu spielen.
Wenn der Polyeder aber eingeschlagen ist, schlägt der Körper ein und das Programm ist beendet. Er wird nicht nach einem erneuten Spielen gefragt, da der Spieler im Spiel nicht mehr existiert.

## 2. Architekturbeschreibung

### 2.1 Projektstruktur

### 2.2 Hauptmodule

### 2.3 Zusammenspiel

## Quellen

- [Coverage](https://coverage.readthedocs.io/en/7.13.5/)
- [Johnson-Körper](https://de.wikipedia.org/wiki/Johnson-K%C3%B6rper)
