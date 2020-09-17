from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

class Form(FlaskForm):
    frage1 = RadioField(u'Welche strategische Ziele verfolgen <br> Sie mit dem Subscription Geschäftsmodell?',
                                    coerce=int, choices=[(1, 'Finanzierungsmodell (Kundensegment erweitern)'),
                                                         (2, 'Kundenanforderung erfüllen'),
                                                         (3, 'Kundenzufriedenheit erhöhen'),
                                                         (4, 'Eigene Wettbewerbsfähigkeit steigern'),
                                                         (5, 'Performancesteigerung mit und für den Kunden')])
    frage2 = RadioField(u'Mit welchen Leistungen können Sie <br> dem Kunden den meisten Mehrwert bieten?',
                                    coerce=int, choices=[(1, 'Verbesserungen am Produkt'),
                                                         (2, 'Ausbau des After-Sales-Service'),
                                                         (3, 'Optimierung des Energieverbrauchs'),
                                                         (4, 'Garantie einer Leistung'),
                                                         (5, 'Übernahme des Betriebs')])
    frage3 = RadioField(u'Über welche IT-Infrastruktur verfügen Sie?',
                                    coerce=int, choices=[(1, 'Unsere Produkte werden datentechnisch nicht erfasst'),
                                                         (2, 'Statische Basisdaten zu jedem verkauften Produkt liegen vor'),
                                                         (3, 'Wir erhalten regelmäßig Zustandsdaten über unsere Wartungsteams'),
                                                         (4, 'Zustandsdaten können digital abgerufen werden'),
                                                         (5, 'Einsatz und Nutzungsprofile können digital abgerufen werden')])
    frage4 = RadioField(u'Wie bewerten Sie Ihre Releasefähigkeit und Service-Struktur?',
                                    coerce=int, choices=[(1, 'Für unsere Produkte wird kein Service angeboten'),
                                                         (2, 'Ersatzteile und Instandhaltung wird über externe Partner abgewickelt'),
                                                         (3, 'Ersatzteile und Instandhaltung wird für einen Teil der Kunden selbst angeboten'),
                                                         (4, 'Ersatzteile und Instandhaltung wird für alle Kunden selbst angeboten'),
                                                         (5, 'Darüber hinaus werden auch datenbasierte Dienstleistungen angeboten')])
    frage5 = RadioField(u'Welche Vertriebsstruktur haben Sie?',
                                    coerce=int, choices=[(1, 'Unser Vertrieb ist über ein mehrstufiges Händlernetz organisiert'),
                                                         (2, 'Wir haben feste Partner für den Vertrieb'),
                                                         (3, 'Neben Vertriebspartnern bieten wir auch einen Direktvertrieb an'),
                                                         (4, 'Für wichtige Kunden haben wir einen Customer Success Manager etabliert'),
                                                         (5, 'Unsere gesamte Organisation ist auf den Kundenerfolg ausgerichtet')])
    frage6 = RadioField(u'Welche Finanzierungslösungen bieten Sie an?',
                                    coerce=int, choices=[(1, 'Kunden können unsere Produkte bar kaufen'),
                                                        (3, 'Wir bieten Kunden eigene Finanzierungslösungen an'),
                                                        (5, 'Es gibt externe Partner für die Finanzierung')])

    submit = SubmitField('Ergebnis anzeigen')