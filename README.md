# Slightly Intrusive Sitater

Savner du å bli kalt homse? Blir du ikke truet på livet for å ikke frikke nok tequils? Utvid din
eksisterende toolbar med denne modulen, for å få velkjente gullkorn fra mjukvarelauget - eller fra
din egen liste hvis du er ei dåse.

# Features (ikke nødvendigvis implementert)

- Støtte for flere bars
    - polybar
    - xmobar
    - windows
    - lemonbar
    - i3bar
- Bilder på notifications
- farget tekst
- Utbyttbare sitatlister

# I aksjon

![aksjonsbilete](https://i.imgur.com/BnrHTH8.png)

# How to

## Polybar
Legg til

```
[module/motivation]
type = custom/script
exec = python /path/til/motivation.py
tail = false
interval = 450
```


I konfigurasjonsfilen, blant de andre modul-definisjonene. Denne finnes ofte i `~/.config/polybar/`. interval-verdien kan endres til ønsket frekvens.\
I samme fil, legg til `motivation` i modulene til baren din, for eksempel som

```
[bar/main]
modules-left = wlan cpu volume
modules-center = i3
modules-right = motivation filesystem battery date
```

## Xmobar
Legg til

```
Run Com "python" ["/path/til/motivation.py"] "motivation" 450
```

i `commands`-listen til `Config`-objektet. Husk deretter å legge til `%motivation%` på ønsket sted i
`template`-verdien. Igjen, kan tallet 450 endres for å sette ønsket frekvens.

