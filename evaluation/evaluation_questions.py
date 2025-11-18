EVAL_DATA: list[dict[str, str]] = [

    # ------------------------------------------------------------
    # 1–25 (Inference + Cross Concept + Real-Life Application)
    # ------------------------------------------------------------

    {
        "question": "Warum führt laut Text die Verstrickung mit dem Veränderlichen dazu, dass Menschen keinen Frieden finden?",
        "ground_truth": "Weil die Orientierung an vergänglichen Eindrücken verhindert, dass Botschaften mit dem Herzen empfangen werden, wodurch kein Zugang zur inneren Wahrheit entsteht."
    },

    {
        "question": "Wie hängt die Fähigkeit, Botschaften mit dem Herzen zu empfangen, mit der Höhe der persönlichen Verdienste zusammen?",
        "ground_truth": "Je größer die Verdienste, desto leichter gelingt es, Botschaften im Herzen aufzunehmen, weil ein ausgeglichener innerer Zustand entsteht."
    },

    # {
    #     "question": "Warum verstärkt eine starke Identitätsbindung die Tendenz, andere zu verurteilen?",
    #     "ground_truth": "Weil feste Selbstbilder zur starren Wahrnehmung führen, wodurch auch andere nur durch alte innere Bilder betrachtet werden."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass negative Bilder über eine Person plötzlich verschwinden können?",
    #     "ground_truth": "Weil gewachsene Verdienste und Segen die inneren Bilder transformieren und dadurch Groll und Anhaftungen auflösen."
    # },

    # {
    #     "question": "Warum verhindert die erste Stufe des Bewusstseins häufig, dass Menschen neue Rollen annehmen können?",
    #     "ground_truth": "Weil auf dieser Stufe das Selbstbild bereits festgelegt ist und daher Veränderung blockiert wird."
    # },

    # {
    #     "question": "Wie beeinflusst der Charakter 'Sich_Vorstellen' den Prozess der Anhäufung im Unterbewusstsein?",
    #     "ground_truth": "Er projiziert innere Bilder in Vergangenheit, Gegenwart und Zukunft, wodurch diese bei wiederholter Aktivierung im Unterbewusstsein gespeichert werden."
    # },

    # {
    #     "question": "Warum kann jemand trotz hoher Intelligenz Schwierigkeiten haben, mit dem Herzen zu hören?",
    #     "ground_truth": "Weil Herzempfang nicht auf Wissen basiert, sondern auf innerer Ausgeglichenheit und Verdiensten."
    # },

    # {
    #     "question": "Wie wird laut Text verhindert, dass eine Person in einer Rolle wie 'Vater' oder 'Arbeiter' gefangen bleibt?",
    #     "ground_truth": "Indem man auf Stufe 3 die Leerheit des Selbst erkennt und Rollen als veränderbare Konzepte versteht."
    # },

    # {
    #     "question": "Warum ist das Herz im Ablauf der inneren Reaktion vor Charakter und Gefühl gesetzt?",
    #     "ground_truth": "Weil nur das Herz empfangen kann, ohne von alten inneren Bildern und Anhäufungen verzerrt zu werden."
    # },

    # {
    #     "question": "Wie hängt Groll mit dem Prinzip der Anhäufung zusammen?",
    #     "ground_truth": "Groll entsteht aus wiederholten negativen Botschaften, die im Unterbewusstsein gespeichert werden und das Bewusstsein verzerren."
    # },

    # {
    #     "question": "Welche Verbindung besteht zwischen Stufe 3 der Weisheit und der Fähigkeit, Talente richtig zu fördern?",
    #     "ground_truth": "Auf Stufe 3 sieht man Menschen frei von alten Bildern, wodurch Entwicklung ungehindert möglich wird."
    # },

    # {
    #     "question": "Wie führt das Festhalten an alten Eindrücken zu falschen Entscheidungen im Alltag?",
    #     "ground_truth": "Weil die Reaktion nicht auf Herzempfang beruht, sondern auf alten gespeicherten Bildern im Unterbewusstsein."
    # },

    # {
    #     "question": "Warum kann ein Mensch trotz guten Willens nicht positiv über jemanden denken?",
    #     "ground_truth": "Weil positives Bewusstsein laut Text von Verdiensten und Segen abhängt, nicht vom Willen allein."
    # },

    # {
    #     "question": "Wie verstärkt der Charakter 'Bewusstsein' die Wirkung des Herzempfangs?",
    #     "ground_truth": "Er erlaubt die klare Unterscheidung nach dem Herzempfang und verhindert impulsive emotionale Reaktionen."
    # },

    # {
    #     "question": "Warum ist übermäßige Ausgeglichenheit problematisch für Wachstum?",
    #     "ground_truth": "Weil sie Motivation und innere Bewegung reduziert, wodurch Entwicklung stagniert."
    # },

    # {
    #     "question": "Wie ermöglicht die zweite Stufe der Weisheit die praktische Umsetzung der dritten Stufe?",
    #     "ground_truth": "Indem sie ein konkretes Bild schafft, das aus der leeren Wahrnehmung der Stufe 3 hervorgeht."
    # },

    # {
    #     "question": "Wie wirkt das Konzept der Leerheit auf zwischenmenschliche Beziehungen?",
    #     "ground_truth": "Es löst vorgefertigte Bilder und Erwartungen auf und erlaubt, Menschen im Jetzt unverzerrt wahrzunehmen."
    # },

    # {
    #     "question": "Warum wird im Text betont, dass Menschen Herausforderungen und keine Probleme sind?",
    #     "ground_truth": "Weil ein Mensch mit großem Segen Situationen aus Gelassenheit betrachtet und nicht als Bedrohung."
    # },

    # {
    #     "question": "Welcher Zusammenhang besteht zwischen innerem Zustand und der Fähigkeit, Weisheit umzusetzen?",
    #     "ground_truth": "Ein ausgeglichener innerer Zustand schafft die Voraussetzung, die drei Stufen der Weisheit bewusst zu durchlaufen."
    # },

    # {
    #     "question": "Warum kann ein Kind sich nicht entwickeln, wenn Eltern an alten Bildern festhalten?",
    #     "ground_truth": "Weil die Identitätsbindung das Kind auf eine Vergangenheit reduziert, die seine Entwicklung einschränkt."
    # },

    # {
    #     "question": "Wie wirken Verdienste auf die Fähigkeit, sich selbst neu zu gestalten?",
    #     "ground_truth": "Sie erhöhen Ausgeglichenheit und innere Klarheit, wodurch neue Selbstbilder stabiler entstehen."
    # },

    # {
    #     "question": "Was passiert, wenn Botschaften primär durch die Ebene des Gefühls gehen?",
    #     "ground_truth": "Sie werden verzerrt, da Gefühle reaktiv sind und nicht aus der inneren Wahrheit entspringen."
    # },

    # {
    #     "question": "Warum ist der erste Schritt jeder Transformation, sich selbst als 'niemand' zu sehen?",
    #     "ground_truth": "Weil Identitätslosigkeit die Voraussetzung dafür ist, ein neues Selbstbild zu formen."
    # },

    # {
    #     "question": "Wie hängt die Fähigkeit zur Toleranz direkt mit Segen zusammen?",
    #     "ground_truth": "Segen erzeugt inneren Reichtum, der Gelassenheit und Mitgefühl ermöglicht."
    # },

    # {
    #     "question": "Was ist der entscheidende Unterschied zwischen Hören mit Herz und Hören mit Charakter?",
    #     "ground_truth": "Herzempfang ist unmittelbar und rein, während Charakteranalysen bereits durch vergangene Anhäufungen gefärbt sind."
    # },

    # # ------------------------------------------------------------
    # # 26–50 (Inference + Cross Concept + Real-Life Application)
    # # ------------------------------------------------------------

    # {
    #     "question": "Warum kann ein innerlich unausgeglichener Mensch selbst bei klaren Botschaften nicht richtig reagieren?",
    #     "ground_truth": "Weil ohne Ausgeglichenheit Botschaften nicht zuerst das Herz erreichen und daher durch Gefühl oder Charakter verzerrt werden."
    # },

    # {
    #     "question": "Wie beeinflusst das Konzept der Anhäufung die Art und Weise, wie Menschen andere beurteilen?",
    #     "ground_truth": "Gespeicherte innere Bilder bestimmen die Wahrnehmung und erzeugen voreilige Urteile."
    # },

    # {
    #     "question": "Warum betont der Text, dass viele Menschen Botschaften nicht direkt empfangen können?",
    #     "ground_truth": "Weil alte Eindrücke aus Vergangenheit und innerer Anhäufung den Herzempfang blockieren."
    # },

    # {
    #     "question": "Wie verstärkt das Festhalten an Rollen wie 'Mutter' oder 'Vater' die emotionale Reaktivität?",
    #     "ground_truth": "Weil Identitätsbindung Erwartungen erzeugt, die Gefühle schneller auslösen als Herzempfang."
    # },

    # {
    #     "question": "Wie beeinflussen Verdienste die Geschwindigkeit, mit der sich negative Bilder über Menschen auflösen?",
    #     "ground_truth": "Je größer die Verdienste, desto schneller wandeln sich alte Bilder, da das Unterbewusstsein gereinigt wird."
    # },

    # {
    #     "question": "Warum ist laut Text die Ordnung 'Herz → Charakter → Gefühl' essenziell für bewusste Reaktionen?",
    #     "ground_truth": "Weil diese Reihenfolge Verzerrungen verhindert und Analyse und Emotion erst nach reinem Empfang stattfinden sollten."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass Menschen trotz Wissen oft falsche Entscheidungen treffen?",
    #     "ground_truth": "Weil Wissen aus Charakter stammt, während Entscheidungen ohne Herzempfang auf alten Anhäufungen basieren."
    # },

    # {
    #     "question": "Warum führt die dritte Stufe der Weisheit zur Freiheit von Bewertungen?",
    #     "ground_truth": "Weil die Wahrnehmung auf dieser Stufe Leerheit erkennt und nicht an Identität oder Vergangenheit haftet."
    # },

    # {
    #     "question": "Wie begünstigt der Charakter 'Reichtum' die innere Entwicklung?",
    #     "ground_truth": "Er verankert Talent und Fähigkeiten, die bei der Umsetzung der drei Weisheitsstufen unterstützen."
    # },

    # {
    #     "question": "Warum entstehen Missverständnisse oft aus dem Charakter 'Sich_Vorstellen'?",
    #     "ground_truth": "Weil unbewusste Projektionen aus Vergangenheit oder Zukunft den klaren Herzempfang überlagern."
    # },

    # {
    #     "question": "Was verhindert, dass ein Mensch sich nicht mehr mit seinem alten Selbstbild identifiziert?",
    #     "ground_truth": "Die Bewusstheit der Stufe 3, die alle Selbstbilder als leer erkennt."
    # },

    # {
    #     "question": "Warum ist die zweite Stufe der Weisheit eine Voraussetzung für Veränderung im Leben?",
    #     "ground_truth": "Weil erst durch ein neues inneres Bild eine neue Ausrichtung und Handlung möglich wird."
    # },

    # {
    #     "question": "Wie hängt das Gefühl der Freude beim Empfang einer Botschaft mit innerem Zustand zusammen?",
    #     "ground_truth": "Freude entsteht, wenn das Herz empfängt, da der innere Zustand harmonisch ist."
    # },

    # {
    #     "question": "Warum können Talente laut Text nur wachsen, wenn man sie regelmäßig auf Stufe 3 zurückführt?",
    #     "ground_truth": "Weil Stufe 3 alte Bilder neutralisiert und Entwicklung ohne Vorurteile ermöglicht."
    # },

    # {
    #     "question": "Warum erzeugt Groll langfristig Leid im Bewusstsein?",
    #     "ground_truth": "Weil sich negative Bilder ansammeln und das Unterbewusstsein mit destruktiven Mustern füllen."
    # },

    # {
    #     "question": "Wie beeinflusst der Charakter 'Ruhm' die Wahrnehmung anderer Menschen?",
    #     "ground_truth": "Er kann Bewertung und Anhaftung verstärken, wodurch Herzempfang erschwert wird."
    # },

    # {
    #     "question": "Warum führt die Arbeit mit der dritten Stufe der Weisheit zu besserem emotionalem Gleichgewicht?",
    #     "ground_truth": "Weil man Identitäten loslässt und dadurch Gefühle weniger reaktiv werden."
    # },

    # {
    #     "question": "Wie unterstützt der Charakter 'Bewusstsein' die Transformation negativer Anhäufungen?",
    #     "ground_truth": "Er ermöglicht klares Erkennen und Unterscheiden nach dem Herzempfang."
    # },

    # {
    #     "question": "Warum wird betont, dass Ausgeglichenheit nicht zu extrem sein darf?",
    #     "ground_truth": "Weil übermäßige Ruhe das Streben nach Wachstum und Handeln hemmt."
    # },

    # {
    #     "question": "Wie verbindet der Text das Prinzip des Unterbewusstseins mit der Fähigkeit, andere zu verstehen?",
    #     "ground_truth": "Angehäufte Bilder formen Wahrnehmung; ein gereinigtes Unterbewusstsein ermöglicht echtes Verstehen."
    # },

    # {
    #     "question": "Wie kann ein Coach laut Text einen Klienten aus Identitätsverhaftung herausführen?",
    #     "ground_truth": "Indem er ihn auf Stufe 3 bringt, leer wahrnehmen lässt und dann ein neues Selbstbild auf Stufe 2 entwickelt."
    # },

    # {
    #     "question": "Warum fällt es Menschen schwer, Veränderungen anderer zu akzeptieren?",
    #     "ground_truth": "Weil alte innere Bilder sie daran hindern, den aktuellen Zustand der Person zu sehen."
    # },

    # {
    #     "question": "Warum verstärkt mangelnder Segen die Tendenz, sich selbst als Opfer zu sehen?",
    #     "ground_truth": "Weil ein schwacher innerer Zustand zu verzerrten Bildern und emotionaler Reaktivität führt."
    # },

    # {
    #     "question": "Wie hängt Stufe 1 der Weisheit mit täglicher Lebenspraxis zusammen?",
    #     "ground_truth": "Sie beschreibt konkretes Tun und Lassen, das notwendig ist, um ein inneres Bild zu verwirklichen."
    # },

    # {
    #     "question": "Warum kann ein Mensch, der stets durch Gefühle reagiert, schwer eine stabile Identität aufbauen?",
    #     "ground_truth": "Weil Gefühle ohne Herzempfang reaktiv und instabil sind und die Anhäufung chaotisch machen."
    # },

    # # ------------------------------------------------------------
    # # 51–75 (Inference + Cross Concept + Coaching Application)
    # # ------------------------------------------------------------

    # {
    #     "question": "Warum erzeugt das Festhalten an einer festen Selbstidentität laut Text innere Unfreiheit?",
    #     "ground_truth": "Weil Identitätsbindung verhindert, sich als veränderbar oder leer wahrzunehmen, wodurch Entwicklung blockiert wird."
    # },

    # {
    #     "question": "Wie beeinflusst die Reinheit des Herzempfangs die Klarheit der Analyse auf der Ebene des Charakters?",
    #     "ground_truth": "Reiner Herzempfang liefert unverzerrte Informationen, sodass Charakteranalyse korrekt und ohne alte Projektionen erfolgt."
    # },

    # {
    #     "question": "Warum ist es für Coaches entscheidend, die Reihenfolge Herz–Charakter–Gefühl zu verstehen?",
    #     "ground_truth": "Weil Coaching auf unverzerrter Wahrnehmung basiert und erst danach Analyse und Emotion sinnvoll sind."
    # },

    # {
    #     "question": "Wie kann ein Coach erkennen, dass ein Klient Botschaften ausschließlich über Gefühle verarbeitet?",
    #     "ground_truth": "An impulsiven, verzerrten Reaktionen und dem Fehlen innerer Klarheit nach dem Empfang."
    # },

    # {
    #     "question": "Warum führt die dritte Stufe der Weisheit zu weniger Missverständnissen in Beziehungen?",
    #     "ground_truth": "Weil man andere ohne alte Bilder sieht und dadurch klarer versteht, was sie wirklich ausdrücken."
    # },

    # {
    #     "question": "Wie hängt der Verlust negativer innerer Bilder mit dem Prinzip der Anhäufung zusammen?",
    #     "ground_truth": "Neue positive Anhäufungen überschreiben alte Muster, wodurch negative Bilder verschwinden."
    # },

    # {
    #     "question": "Warum wird im Text betont, dass Menschen Botschaften mit ‚innerer Freude‘ sehen können?",
    #     "ground_truth": "Weil Herzempfang in Ausgeglichenheit geschieht und innere Freude ein natürlicher Zustand dieser Reinheit ist."
    # },

    # {
    #     "question": "Wie schafft die zweite Stufe der Weisheit eine Brücke zwischen Leerheit und praktischer Handlung?",
    #     "ground_truth": "Indem sie aus leerer Wahrnehmung ein konkretes Bild formt, das dann in Stufe 1 umgesetzt wird."
    # },

    # {
    #     "question": "Warum reagiert ein Mensch mit wenig Verdiensten schneller gereizt?",
    #     "ground_truth": "Weil ein schwacher innerer Zustand dazu führt, dass Botschaften nicht das Herz erreichen und daher über Gefühle verzerrt werden."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass viele Menschen unbewusst im Modus der Vergangenheit leben?",
    #     "ground_truth": "Weil sich ihre Wahrnehmung aus angehäuften alten Eindrücken speist, nicht aus dem aktuellen Herzempfang."
    # },

    # {
    #     "question": "Warum sind gespeicherte innere Bilder mächtiger als frische Sinneseindrücke?",
    #     "ground_truth": "Weil sie tief im Unterbewusstsein verankert sind und Wahrnehmung automatisch formen."
    # },

    # {
    #     "question": "Wie beeinflusst der Charakter 'Gier' den Zugang zur echten Wahrheit?",
    #     "ground_truth": "Er schafft starke emotionale Verzerrungen, die das Herz blockieren und Wahrnehmung trüben."
    # },

    # {
    #     "question": "Wie wirkt ständiges inneres Verurteilen auf das Unterbewusstsein?",
    #     "ground_truth": "Es erzeugt wiederholte negative Anhäufungen, die langfristig das Bewusstsein trüben."
    # },

    # {
    #     "question": "Warum ist die Arbeit auf Stufe 3 besonders schwer für Menschen mit starkem Ego?",
    #     "ground_truth": "Weil starke Ego-Identität direkt im Widerspruch zur Leerheit steht und diese nicht anerkennen kann."
    # },

    # {
    #     "question": "Wie kann ein Coach erkennen, ob ein Klient bereits auf Stufe 2 arbeitet?",
    #     "ground_truth": "Wenn der Klient ein bewusst formuliertes Bild seiner zukünftigen Version entwickelt."
    # },

    # {
    #     "question": "Warum kann ein Mensch trotz äußerem Erfolg innerlich instabil bleiben?",
    #     "ground_truth": "Weil Erfolg aus Charakter oder Fähigkeiten stammen kann, während innerer Zustand und Verdienste fehlen."
    # },

    # {
    #     "question": "Wie zeigt sich die Wirkung des Charakters 'Bewusstsein' im Alltag?",
    #     "ground_truth": "Er ermöglicht klare Unterscheidung nach Herzempfang und verhindert falsche emotionale Schlüsse."
    # },

    # {
    #     "question": "Warum kann zu starke Identifikation mit Schönheit laut Text hinderlich sein?",
    #     "ground_truth": "Weil äußere Erscheinung dann zum selbstdefinierten Maßstab wird, was zu verzerrter Wahrnehmung führt."
    # },

    # {
    #     "question": "Wie beeinflusst ein Mangel an Dankbarkeit den inneren Zustand?",
    #     "ground_truth": "Er senkt den inneren Schwingungszustand und erschwert Herzempfang und Ausgeglichenheit."
    # },

    # {
    #     "question": "Warum ist das Prinzip 'Menschen sind Herausforderungen, keine Probleme' transformativ?",
    #     "ground_truth": "Weil es die Wahrnehmung von Bedrohung zu Entwicklungsmöglichkeit verschiebt, was Gelassenheit erzeugt."
    # },

    # {
    #     "question": "Warum reagiert ein Mensch ruhiger, wenn er sein Gegenüber als 'niemand' sieht?",
    #     "ground_truth": "Weil dies innere Erwartungen und alte Bilder entfernt und Herzempfang erleichtert."
    # },

    # {
    #     "question": "Wie hindert der Charakter 'Ruhm' Menschen an ehrlicher Selbstreflexion?",
    #     "ground_truth": "Weil Anhaftung an Anerkennung Bilder über sich selbst festigt und die Leerheit blockiert."
    # },

    # {
    #     "question": "Warum macht ein reaktives Unterbewusstsein eine langfristige Selbstveränderung schwierig?",
    #     "ground_truth": "Weil neue Bilder nicht stabil aufgenommen werden, wenn alte emotionale Muster dominieren."
    # },

    # {
    #     "question": "Wie sind Herzempfang und der Prozess der Anhäufung miteinander verbunden?",
    #     "ground_truth": "Herzempfang filtert Botschaften rein; ohne ihn sammelt sich verzerrter Inhalt im Unterbewusstsein an."
    # },

    # {
    #     "question": "Warum ist das Verstehen der drei Stufen der Weisheit essentiell für Eltern laut Text?",
    #     "ground_truth": "Weil es hilft, Kinder frei von alten Bildern zu sehen und ihre Entwicklung bewusst zu begleiten."
    # },

    # # ------------------------------------------------------------
    # # 76–100 (Inference + Cross Concept + Coaching Application)
    # # ------------------------------------------------------------

    # {
    #     "question": "Wie erklärt der Text, dass ein Mensch trotz langjähriger spiritueller Praxis innerlich instabil bleiben kann?",
    #     "ground_truth": "Weil Stabilität aus Herzempfang, Verdiensten und Ausgeglichenheit entsteht und nicht aus Wissen oder Übung allein."
    # },

    # {
    #     "question": "Warum verstärkt der Charakter 'Sich_Vorstellen' innere Konflikte, wenn er nicht vom Herzempfang begleitet wird?",
    #     "ground_truth": "Weil Projektionen entstehen, die vergangenheits- oder zukunftsbasiert sind und nicht der realen Botschaft entsprechen."
    # },

    # {
    #     "question": "Wie erklärt das Modell der drei Stufen der Weisheit, warum Menschen ihre eigenen Ziele oft sabotieren?",
    #     "ground_truth": "Weil sie ohne Stufe 3 an alten Selbstbildern haften und ohne Stufe 2 kein neues inneres Bild formen."
    # },

    # {
    #     "question": "Warum führt fehlender Herzempfang im Alltag häufig zu Überinterpretation?",
    #     "ground_truth": "Weil Charakter und Gefühl auf alte Anhäufungen zurückgreifen und dadurch Botschaften verzerren."
    # },

    # {
    #     "question": "Wie unterstützt die dritte Stufe der Weisheit die emotionale Heilung?",
    #     "ground_truth": "Sie löst Identität und damit auch die Anhaftung an verletzte Selbstbilder."
    # },

    # {
    #     "question": "Warum erzeugt der Charakter 'Gier' langfristig Instabilität im Unterbewusstsein?",
    #     "ground_truth": "Weil er Anhäufungen aus Begierde erzeugt, die Emotionen verstärken und Herzempfang verhindern."
    # },

    # {
    #     "question": "Wie kann ein Coach laut Text erkennen, dass ein Klient im Unterbewusstsein negative Anhäufungen trägt?",
    #     "ground_truth": "An unverhältnismäßig emotionalen Reaktionen, die nicht zum aktuellen Ereignis passen."
    # },

    # {
    #     "question": "Warum wird im Text betont, dass Weisheit sichtbar im äußeren Erscheinungsbild wird?",
    #     "ground_truth": "Weil innere Ausgeglichenheit und Herzempfang sich automatisch in Haltung, Mimik und Verhalten zeigen."
    # },

    # {
    #     "question": "Wie verhindert Identität, dass eine Person das Potenzial der dritten Weisheitsstufe nutzt?",
    #     "ground_truth": "Identität hält am Bild 'ich bin jemand' fest und widerspricht dem leeren Selbstverständnis auf Stufe 3."
    # },

    # {
    #     "question": "Wie erklärt der Text die Entstehung von Konflikten zwischen Menschen aus Sicht der Anhäufung?",
    #     "ground_truth": "Konflikte entstehen, wenn unterschiedliche alte innere Bilder aufeinanderprallen und Herzempfang fehlt."
    # },

    # {
    #     "question": "Warum fällt es manchen Menschen schwer, Dankbarkeit zu empfinden, selbst wenn es ihnen gut geht?",
    #     "ground_truth": "Weil Verdienste und Segen fehlen, die den inneren Zustand für Dankbarkeit öffnen."
    # },

    # {
    #     "question": "Wie verstärkt ständiges Denken über die Vergangenheit die Identitätsbindung?",
    #     "ground_truth": "Weil das Unterbewusstsein alte Bilder wiederholt aktualisiert und so das Selbstbild fixiert wird."
    # },

    # {
    #     "question": "Warum ist es laut Text gefährlich, Botschaften primär über den Charakter zu empfangen?",
    #     "ground_truth": "Weil der Charakter mit alten Bildern arbeitet und daher die ursprüngliche Botschaft verzerrt."
    # },

    # {
    #     "question": "Warum erzeugen Menschen oft Leiden, obwohl sie objektiv im Recht sind?",
    #     "ground_truth": "Weil das Leiden nicht vom Ereignis stammt, sondern von inneren Anhäufungen und Groll."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass Veränderung erst möglich wird, wenn man sich selbst als 'niemand' sieht?",
    #     "ground_truth": "Weil nur Leerheit Raum für ein neues Selbstbild schafft, ohne an alten Identitäten zu haften."
    # },

    # {
    #     "question": "Warum reagiert ein Mensch mit hohem Segen konstruktiver auf Angriffe?",
    #     "ground_truth": "Weil sein Herzempfang stabil ist und er Botschaften ohne Verzerrung wahrnimmt."
    # },

    # {
    #     "question": "Wie beeinflusst innere Freude den Prozess der Anhäufung?",
    #     "ground_truth": "Freude erzeugt positive Anhäufungen, die das Unterbewusstsein stabilisieren."
    # },

    # {
    #     "question": "Warum behindert zu viel Selbststolz die innere Entwicklung?",
    #     "ground_truth": "Weil Stolz an Identität bindet und Stufe-3-Leerheit blockiert."
    # },

    # {
    #     "question": "Wie trägt der Charakter 'Bewusstsein' dazu bei, alte Muster zu durchbrechen?",
    #     "ground_truth": "Durch klare Unterscheidung nach Herzempfang erkennt man Muster und handelt bewusst statt automatisch."
    # },

    # {
    #     "question": "Warum beeinflusst ein negativer innerer Schwingungszustand die Entscheidungen im Alltag?",
    #     "ground_truth": "Weil Botschaften dann über Gefühle oder negative Anhäufungen gelangen und Entscheidungen verzerrt werden."
    # },

    # {
    #     "question": "Wie unterstützt Stufe 2 der Weisheit Personen, die sich unterbewusst selbst limitieren?",
    #     "ground_truth": "Sie erzeugt ein neues Zielbild, das alte limitierende Bilder überschreiben kann."
    # },

    # {
    #     "question": "Warum entstehen in Beziehungen oft wiederkehrende Konfliktschleifen?",
    #     "ground_truth": "Weil beide Personen aus ihren alten Anhäufungen reagieren und Herzempfang fehlt."
    # },

    # {
    #     "question": "Wie erklärt der Text den Zusammenhang zwischen Segen und der Fähigkeit, Herausforderungen anzunehmen?",
    #     "ground_truth": "Segen macht den inneren Zustand ruhig, wodurch Herausforderungen als Entwicklungsmöglichkeiten gesehen werden."
    # },

    # {
    #     "question": "Warum ist Herzempfang laut Text der einzige Weg zu echter Erkenntnis?",
    #     "ground_truth": "Weil nur das Herz unverzerrte Botschaften liefert, während Charakter und Gefühl durch Vergangenheit beeinflusst sind."
    # },

    # {
    #     "question": "Wie verhindert das Prinzip der Leerheit, dass man andere kontrolliert oder bewertet?",
    #     "ground_truth": "Weil Leerheit jede feste Identität auflöst, wodurch Kontrolle und Bewertung ihren inneren Ursprung verlieren."
    # },

    # # ------------------------------------------------------------
    # # 101–200 (zweites 100er Paket – sehr tief, sehr komplex)
    # # ------------------------------------------------------------

    # {
    #     "question": "Wie erklärt der Text, dass Menschen oft glauben, sie seien objektiv, obwohl ihre Wahrnehmung vom Unterbewusstsein gefärbt ist?",
    #     "ground_truth": "Weil alte Anhäufungen im Unterbewusstsein automatisch die Wahrnehmung formen, ohne dass Menschen dies bemerken."
    # },

    # {
    #     "question": "Warum ist laut Text die Fähigkeit, Botschaften mit dem Herzen zu empfangen, ein Indikator für spirituelle Reife?",
    #     "ground_truth": "Weil Herzempfang nur bei ausgeglichenem inneren Zustand möglich ist, der aus Verdiensten und Segen entsteht."
    # },

    # {
    #     "question": "Wie führt Identitätsverhaftung zu automatischen emotionalen Reaktionen?",
    #     "ground_truth": "Weil Identität alte Bilder stärkt, die Gefühle vor dem Herzempfang aktivieren."
    # },

    # {
    #     "question": "Warum ist laut Text wahre Freude unabhängig von äußeren Umständen?",
    #     "ground_truth": "Weil Freude aus Herzempfang entsteht, der inneren Frieden erzeugt, nicht aus äußeren Reizen."
    # },

    # {
    #     "question": "Wie verhindert die dritte Stufe der Weisheit, dass Menschen andere aufgrund ihrer Vergangenheit beurteilen?",
    #     "ground_truth": "Weil Stufe 3 die Leerheit des Selbst erkennt und dadurch alte Bilder auflöst."
    # },

    # {
    #     "question": "Warum führt das Bilden eines neuen Selbst auf Stufe 2 nicht zu Illusion, sondern zu Transformation?",
    #     "ground_truth": "Weil es ein bewusstes, aus Stufe 3 abgeleitetes Bild ist, das durch Verhalten realisiert wird."
    # },

    # {
    #     "question": "Wie ist die Tendenz, sich selbst zu schützen, mit fehlendem Herzempfang verbunden?",
    #     "ground_truth": "Weil Schutzmechanismen aus alten Anhäufungen stammen, die aktiv werden, wenn Herzempfang fehlt."
    # },

    # {
    #     "question": "Warum erzeugt mangelnde Dankbarkeit eine geringere Schwingungsfrequenz?",
    #     "ground_truth": "Weil Undankbarkeit den inneren Zustand senkt und Ausgeglichenheit verhindert."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass wahre Entwicklung immer mit Loslassen beginnt?",
    #     "ground_truth": "Weil Loslassen Identität und alte Bilder löst, wodurch Stufe 3 zugänglich wird."
    # },

    # {
    #     "question": "Warum können zwei Menschen dieselbe Botschaft komplett unterschiedlich wahrnehmen?",
    #     "ground_truth": "Weil ihre Anhäufungen, Verdienste und inneren Zustände verschieden sind."
    # },

    # {
    #     "question": "Wie erzeugt der Charakter 'Ruhm' häufig Abhängigkeit von äußerer Anerkennung?",
    #     "ground_truth": "Weil Ruhm als Charakter die Bedeutung des äußeren Bildes verstärkt."
    # },

    # {
    #     "question": "Warum kann jemand trotz starken Wunsches nicht vergeben?",
    #     "ground_truth": "Weil Vergebung aus Verdiensten und Segen entsteht, nicht aus Willenskraft."
    # },

    # {
    #     "question": "Wie führt eine erhöhte Schwingungsfrequenz zu positiverer Wahrnehmung?",
    #     "ground_truth": "Weil ein hoher innerer Zustand klaren Herzempfang ermöglicht."
    # },

    # {
    #     "question": "Warum können starke Emotionen das Unterbewusstsein langfristig prägen?",
    #     "ground_truth": "Weil emotionale Intensität tiefe Anhäufungen erzeugt."
    # },

    # {
    #     "question": "Wie kann Stufe 1 falsch angewendet werden, wenn Stufe 3 fehlt?",
    #     "ground_truth": "Man handelt aus altem Selbstbild und nicht aus leerer, neuer Sicht."
    # },

    # {
    #     "question": "Wie zeigt sich im Alltag, dass ein Mensch zuerst durch Charakter reagiert?",
    #     "ground_truth": "An schnellen, rationalen, aber verzerrten Einordnungen ohne innere Ruhe."
    # },

    # {
    #     "question": "Warum macht ein Mensch mit viel Groll andere für sein Leid verantwortlich?",
    #     "ground_truth": "Weil negative Anhäufungen das Bewusstsein verzerren und Täterrollen erzeugen."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass negative Anhäufungen durch Wiederholung verfestigt werden?",
    #     "ground_truth": "Weil jeder wiederholte Eindruck denselben Weg im Unterbewusstsein verstärkt."
    # },

    # {
    #     "question": "Warum ist Weisheit ein Prozess, der von innen nach außen wirkt?",
    #     "ground_truth": "Weil innere Ausrichtung Verhalten und Wahrnehmung bestimmt."
    # },

    # {
    #     "question": "Wie wirkt die dritte Stufe der Weisheit als Reset für das Unterbewusstsein?",
    #     "ground_truth": "Sie löst Identität und damit die Wurzel alter Anhäufungen auf."
    # },

    # {
    #     "question": "Warum entsteht Leid laut Text oft durch das Festhalten an alten Bildern?",
    #     "ground_truth": "Weil alte Bilder die Wahrnehmung einschränken und Herzempfang verhindern."
    # },

    # {
    #     "question": "Wie beeinflusst der Charakter 'Empfangen' die geistige Entwicklung?",
    #     "ground_truth": "Er ist die Grundlage jeder inneren Transformation, weil er Botschaften rein aufnimmt."
    # },

    # {
    #     "question": "Warum wird ständiges Vergleichen als Anzeichen von Identitätsbindung gesehen?",
    #     "ground_truth": "Weil Vergleichen zeigt, dass man sich über Bilder definiert."
    # },

    # {
    #     "question": "Wie erklärt der Text die Entstehung von Stolz?",
    #     "ground_truth": "Pride entsteht aus Identitätsverhaftung an Rollen oder Selbstbildern."
    # },

    # {
    #     "question": "Warum führt Denken ohne Herzempfang zu Überforderung?",
    #     "ground_truth": "Weil Analyse ohne innere Ruhe von alten Bildern überlagert wird."
    # },

    # {
    #     "question": "Wie hilft Verdienste-Aufbau beim Auflösen emotionaler Trigger?",
    #     "ground_truth": "Weil Verdienste den inneren Zustand stabilisieren und Herzempfang ermöglichen."
    # },

    # {
    #     "question": "Warum sind Menschen mit niedrigem inneren Zustand anfälliger für Missverständnisse?",
    #     "ground_truth": "Weil Botschaften über Gefühlsschichten und nicht über das Herz empfangen werden."
    # },

    # {
    #     "question": "Wie beeinflusst der Charakter 'Schlafen' das geistige Gleichgewicht?",
    #     "ground_truth": "Er stellt die körperliche Ruhe her, die Herzempfang unterstützt."
    # },

    # {
    #     "question": "Warum wird betont, dass Menschen Wahrnehmung nur durch Herzempfang ändern können?",
    #     "ground_truth": "Weil das Herz Zugang zur inneren Wahrheit hat, während Charakter und Gefühl verzerrt sind."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass das Unterbewusstsein nie wirklich ‚leer‘ ist?",
    #     "ground_truth": "Weil es ständig Anhäufung aus Hören, Sehen, Wissen und Sprechen speichert."
    # },

    # {
    #     "question": "Wie entstehen unbewusste Vorurteile laut Text?",
    #     "ground_truth": "Durch lange gespeicherte innere Bilder im Unterbewusstsein."
    # },

    # {
    #     "question": "Warum verschwindet der Impuls zur Kontrolle, wenn man Stufe 3 erreicht?",
    #     "ground_truth": "Weil Leerheit keine festen Erwartungen an sich selbst oder andere erzeugt."
    # },

    # {
    #     "question": "Warum beurteilen Menschen andere oft nach ihrer Vergangenheit?",
    #     "ground_truth": "Weil vergangene Eindrücke im Unterbewusstsein gespeichert bleiben."
    # },

    # {
    #     "question": "Wie hängt Selbstvertrauen mit Herzempfang zusammen?",
    #     "ground_truth": "Herzempfang erzeugt klare innere Führung, die Vertrauen stärkt."
    # },

    # {
    #     "question": "Warum ist es gefährlich, wenn Menschen glauben, Gefühle seien ihre Wahrheit?",
    #     "ground_truth": "Weil Gefühle reaktiv sind und nicht aus innerem Wissen stammen."
    # },

    # {
    #     "question": "Wie erklärt der Text die Entstehung innerer Blockaden?",
    #     "ground_truth": "Durch wiederholte negative Anhäufungen, die Herzempfang erschweren."
    # },

    # {
    #     "question": "Warum können Menschen mit hohem Groll keine klare Vision entwickeln?",
    #     "ground_truth": "Weil negative Schwingungen Stufe 2 verhindern."
    # },

    # {
    #     "question": "Wie entsteht laut Text Vertrauen in andere Menschen?",
    #     "ground_truth": "Durch reinem Herzempfang, der alte Verzerrungen löst."
    # },

    # {
    #     "question": "Warum sind Menschen, die sich als Opfer sehen, besonders stark an Identität gebunden?",
    #     "ground_truth": "Weil ihre Identität auf verletzten inneren Bildern aufgebaut ist."
    # },

    # {
    #     "question": "Wie hängt intuitive Klarheit mit Stufe 3 zusammen?",
    #     "ground_truth": "Stufe 3 erzeugt leere Wahrnehmung, die klare intuitive Einsicht ermöglicht."
    # },

    # {
    #     "question": "Warum erzeugt das Konzept der Leerheit innere Sicherheit?",
    #     "ground_truth": "Weil Sicherheit nicht mehr auf Rollen oder äußere Bedingungen angewiesen ist."
    # },

    # {
    #     "question": "Wie verhindert Gier langfristige Ausgeglichenheit?",
    #     "ground_truth": "Weil sie innere Unruhe und ständige emotionale Schwankungen erzeugt."
    # },

    # {
    #     "question": "Warum ist Herzempfang Voraussetzung für echtes Zuhören?",
    #     "ground_truth": "Weil nur das Herz ohne Verzerrung aufnimmt."
    # },

    # {
    #     "question": "Wie unterstützt Dankbarkeit die Transformation des Unterbewusstseins?",
    #     "ground_truth": "Dankbarkeit erhöht die Schwingung und überschreibt alte negative Anhäufungen."
    # },

    # {
    #     "question": "Warum ist Stufe 3 nicht erreichbar, solange man sich als Opfer einer Situation sieht?",
    #     "ground_truth": "Weil Opferrollen Identität stärken und Leerheit verhindern."
    # },

    # {
    #     "question": "Wie erklärt der Text die Fähigkeit, große Fragen sofort zu verstehen?",
    #     "ground_truth": "Weil Herzempfang schnelle Einsicht ermöglicht."
    # },

    # {
    #     "question": "Warum führt Einfühlungsvermögen zu weniger Stress?",
    #     "ground_truth": "Weil Herzempfang Mitgefühl ermöglicht und emotionale Reaktivität senkt."
    # },

    # # # -----------------------------------------------------
    # # # 1–10: Grundlagen Imagination + Lernen
    # # # -----------------------------------------------------

    # # {
    # #     "question": "Was bedeutet 'Imagination' laut Text im pädagogischen Kontext?",
    # #     "ground_truth": "Das Vermögen des Geistes, innere Bilder hervorzubringen und Gegenstände ohne deren physische Anwesenheit vorzustellen."
    # # },

    # # {
    # #     "question": "Warum ist Imagination für Lernen unverzichtbar?",
    # #     "ground_truth": "Weil Verstehen die Fähigkeit erfordert, Modelle, Zusammenhänge und Situationen innerlich zu repräsentieren."
    # # },

    # # {
    # #     "question": "Wie wird nach Kant die Einbildungskraft beschrieben?",
    # #     "ground_truth": "Als Vermögen, einen Gegenstand auch ohne dessen Gegenwart in der Anschauung vorzustellen."
    # # },

    # # {
    # #     "question": "Warum spricht der Text von einer 'inneren Wirklichkeit' des Lernens?",
    # #     "ground_truth": "Weil Lernen als geistiger Prozess Wahrnehmen, Denken, Vorstellen und Fühlen umfasst."
    # # },

    # # {
    # #     "question": "Welche Rolle spielt die Imagination im Prozess der Wahrnehmung laut Text?",
    # #     "ground_truth": "Sie macht Wahrnehmung zu einer aktiv-produktiven Leistung und nicht zu einer Abbildung der Realität."
    # # },

    # # {
    # #     "question": "Warum wird behauptet, dass moderne Pädagogik die Imagination vernachlässigt?",
    # #     "ground_truth": "Weil systematische Rationalisierung und Faktenfokus imaginative Prozesse verdrängt haben."
    # # },

    # # {
    # #     "question": "Wie erklärt der Text, dass wir uns auch ohne Licht in einer Wohnung zurechtfinden?",
    # #     "ground_truth": "Weil die Wohnung als innere Vorstellung präsent ist."
    # # },

    # # {
    # #     "question": "Warum ist Imagination ein zentrales Moment geistiger Erfahrung?",
    # #     "ground_truth": "Weil sie Denken, Wahrnehmen, Vorstellen und Ich-Bewusstsein verbindet."
    # # },

    # # {
    # #     "question": "Warum lässt sich Verstehen nicht auf logisches Begreifen reduzieren?",
    # #     "ground_truth": "Weil Verstehen Einsicht und Erfahrung in einen übergreifenden Zusammenhang bringt."
    # # },

    # # {
    # #     "question": "Warum muss Imagination in pädagogischen Theorien stärker berücksichtigt werden?",
    # #     "ground_truth": "Weil sie eine zentrale Funktion des Erkennens, Denkens und Handelns darstellt."
    # # },

    # # # -----------------------------------------------------
    # # # 11–20: Verständnisintensives Lernen – Kernprinzipien
    # # # -----------------------------------------------------

    # # {
    # #     "question": "Welche vier Aspekte bilden laut Text die Basis verständnisintensiven Lernens?",
    # #     "ground_truth": "Erfahrung, Vorstellung (Imagination), Begreifen und Metakognition."
    # # },

    # # {
    # #     "question": "Was ist das Ziel verständnisintensiven Lernens?",
    # #     "ground_truth": "Der Aufbau von anwendungsbereitem, flexiblem und intelligentem Wissen und Können."
    # # },

    # # {
    # #     "question": "Warum betont der Text den Prozess des Lernens mehr als die Auswahl von Inhalten?",
    # #     "ground_truth": "Weil Lernen als dynamischer, qualitativer Prozess verstanden wird, nicht als reine Wissensansammlung."
    # # },

    # # {
    # #     "question": "Wie unterscheidet sich Bildung vom bloßen Lernen?",
    # #     "ground_truth": "Bildung verbindet Wissen, Handeln und Urteilen zu selbstständiger, verantwortlicher Mündigkeit."
    # # },

    # # {
    # #     "question": "Warum gehört Metakognition zu den vier Grundelementen verständnisintensiven Lernens?",
    # #     "ground_truth": "Weil sie Reflexion ermöglicht und die eigenen Denk- und Lernprozesse bewusst steuert."
    # # },

    # # {
    # #     "question": "Wie beschreibt der Text das Zusammenspiel der vier Aspekte?",
    # #     "ground_truth": "Als nachhaltiges, produktives, reflexives Zusammenwirken von Erfahrung, Vorstellung, Begreifen und Metakognition."
    # # },

    # # {
    # #     "question": "Warum ist Erfahrung nach dem Text grundlegend für Lernen?",
    # #     "ground_truth": "Weil Lernen aus aktivem Handeln und dem Erleben von Wirklichkeit entsteht."
    # # },

    # # {
    # #     "question": "Was bedeutet die 'Ellipse des praktischen Lernens'?",
    # #     "ground_truth": "Die Verbindung des individuellen Tätigseins mit gesellschaftlichen Tätigkeitsfeldern."
    # # },

    # # {
    # #     "question": "Warum braucht Verstehen nach dem Text sowohl Wahrnehmung als auch Vorstellung?",
    # #     "ground_truth": "Weil sinnliche Eindrücke und innere Modelle gemeinsam Bedeutungen ermöglichen."
    # # },

    # # {
    # #     "question": "Warum gilt verständnisintensives Lernen als 'mehrdimensional'?",
    # #     "ground_truth": "Weil mehrere kognitive und erfahrungsbezogene Ebenen gleichzeitig zusammenwirken."
    # # },

    # # # -----------------------------------------------------
    # # # 21–30: Cross-Concept (Imagination + Bildung + Kritik am Schulsystem)
    # # # -----------------------------------------------------

    # # {
    # #     "question": "Warum kritisiert der Text die 'technisch-rationalisierte' Schule?",
    # #     "ground_truth": "Weil sie Imagination, innere Erfahrung und tiefes Verstehen zugunsten messbarer Fakten vernachlässigt."
    # # },

    # # {
    # #     "question": "Wie führt mangelnde Imagination zu Lernschwierigkeiten?",
    # #     "ground_truth": "Weil ohne innere Bilder keine Modelle, Hypothesen oder Zusammenhänge konstruiert werden können."
    # # },

    # # {
    # #     "question": "Warum ist reproduktives Lernen dem Verständnislernen unterlegen?",
    # #     "ground_truth": "Weil es nur oberflächlich Wissen wiederholt und keine flexiblen geistigen Strukturen aufbaut."
    # # },

    # # {
    # #     "question": "Wie erklärt der Text die Bedeutung von Modellen beim Verstehen?",
    # #     "ground_truth": "Weil komplexe Sachverhalte im Kopf durch hypothetische Modelle erschlossen werden."
    # # },

    # # {
    # #     "question": "Warum beschreibt der Text Verstehen als 'vernunftbezogen'?",
    # #     "ground_truth": "Weil Verstehen das Zusammenführen von Einsicht und Erfahrung voraussetzt."
    # # },

    # # {
    # #     "question": "Wie setzt sich verständnisintensives Lernen von bloßer Wissensvermittlung ab?",
    # #     "ground_truth": "Durch Fokus auf Prozesse, Reflexion, Vorstellungen und aktives Erschließen statt reines Reproduzieren."
    # # },

    # # {
    # #     "question": "Warum bezeichnet der Text Imagination als 'Hervorbringen' und nicht als Abbilden?",
    # #     "ground_truth": "Weil Wahrnehmung konstruktiv und nicht passiv ist."
    # # },

    # # {
    # #     "question": "Welche Folge hat es, wenn Lernende nur Faktenwissen ohne innere Modelle erwerben?",
    # #     "ground_truth": "Das Wissen bleibt unverbunden, instabil und nicht anwendungsfähig."
    # # },

    # # {
    # #     "question": "Warum ist Begreifen eine 'verinnerlichte Greifhandlung'?",
    # #     "ground_truth": "Weil es auf sinnlicher Wahrnehmung aufbaut, aber kognitiv weiterverarbeitet wird."
    # # },

    # # {
    # #     "question": "Wie erklärt der Text die Rolle von kritischer Reflexion beim Verstehen?",
    # #     "ground_truth": "Sie ermöglicht Beurteilung, Korrektur und Grenzen eigener Interpretationen."
    # # },

    # # # -----------------------------------------------------
    # # # 31–40: Coaching-Transfer (Learning → Coaching)
    # # # -----------------------------------------------------

    # # {
    # #     "question": "Wie kann das Konzept des verständnisintensiven Lernens im Coaching angewendet werden?",
    # #     "ground_truth": "Coaching sollte Erfahrung, innere Vorstellung, begriffliches Verstehen und Reflexion verbinden."
    # # },

    # # {
    # #     "question": "Warum scheitern viele Coaching-Informationen ohne Imagination?",
    # #     "ground_truth": "Weil Klienten neue Inhalte nicht innerlich modellieren und dadurch nicht anwenden können."
    # # },

    # # {
    # #     "question": "Wie erklärt der Text, dass bloßes Wissen im Coaching nicht ausreicht?",
    # #     "ground_truth": "Weil Verhaltensänderung erst durch Einsicht, Modelle und reflektierte Erfahrung entsteht."
    # # },

    # # {
    # #     "question": "Warum brauchen Klienten beim Verstehen neuer Verhaltensstrategien mentale Modelle?",
    # #     "ground_truth": "Weil abstrakte Konzepte durch innere Visualisierung anwendbar werden."
    # # },

    # # {
    # #     "question": "Wie hilft Metakognition im Coaching laut Text?",
    # #     "ground_truth": "Sie macht Klienten ihre mentalen Muster bewusst und lenkbar."
    # # },

    # # {
    # #     "question": "Wie lässt sich 'praktisches Lernen' im Coaching nutzen?",
    # #     "ground_truth": "Durch aktives Ausprobieren, Experimentieren und erfahrungsbasierte Interventionen."
    # # },

    # # {
    # #     "question": "Warum sind im Coaching sowohl Erfahrung als auch Vorstellung wichtig?",
    # #     "ground_truth": "Weil reale Erlebnisse und innere Simulationen gemeinsam neue Kompetenzen formen."
    # # },

    # # {
    # #     "question": "Wie unterstützt verständnisintensives Lernen nachhaltige Veränderungsprozesse im Coaching?",
    # #     "ground_truth": "Durch tiefes Durchdringen, Modellbildung und reflektierten Transfer."
    # # },

    # # {
    # #     "question": "Warum ist Faktenfokus im Coaching ähnlich problematisch wie im Schulsystem?",
    # #     "ground_truth": "Weil er keine innere Transformation erzeugt, sondern nur Information anhäuft."
    # # },

    # # {
    # #     "question": "Welche Rolle spielt innere Erfahrung im Umgang mit emotionalen Mustern?",
    # #     "ground_truth": "Sie ermöglicht, Gefühle als innere Realität zu erkennen und bewusst zu verändern."
    # # },

    # # # -----------------------------------------------------
    # # # 41–50: Vertiefung – Imagination, Wahrnehmung, Modelle
    # # # -----------------------------------------------------

    # # {
    # #     "question": "Warum beschreibt der Text Wahrnehmung als aktiv-produktiven Prozess und nicht als passives Abbilden?",
    # #     "ground_truth": "Weil unser Geist Wahrgenommenes konstruktiv erzeugt und nicht einfach kopiert."
    # # },

    # # {
    # #     "question": "Wie erklärt das Beispiel mit der dunklen Wohnung die Rolle innerer Modelle beim Handeln?",
    # #     "ground_truth": "Man bewegt sich sicher, weil die Struktur der Wohnung als innere Vorstellung präsent ist."
    # # },

    # # {
    # #     "question": "Warum ist Imagination laut Text eine Voraussetzung für komplexe Problemlösung?",
    # #     "ground_truth": "Weil Problemlösung das mentale Durchspielen von Situationen, Hypothesen und Modellen erfordert."
    # # },

    # # {
    # #     "question": "Was ist der zentrale pädagogische Wert innerer Bilder?",
    # #     "ground_truth": "Sie ermöglichen tiefes Verstehen durch mentale Repräsentation komplexer Zusammenhänge."
    # # },

    # # {
    # #     "question": "Warum gilt Vorstellungskraft als Bindeglied zwischen Erfahrung und Denken?",
    # #     "ground_truth": "Weil sie Wahrgenommenes innerlich transformiert und für begriffliches Denken verfügbar macht."
    # # },

    # # {
    # #     "question": "Wie begründet der Text, dass Imagination eine Kernfunktion menschlicher Welterschließung ist?",
    # #     "ground_truth": "Sie verbindet Wahrnehmen, Denken, Fühlen und Ich-Bewusstsein zu einer inneren Wirklichkeit."
    # # },

    # # {
    # #     "question": "Warum ist der Begriff der Vorstellung in der Pädagogik unterrepräsentiert?",
    # #     "ground_truth": "Weil moderne Rationalisierung imaginative Prozesse zugunsten messbarer Leistungen verdrängt hat."
    # # },

    # # {
    # #     "question": "Wie erweitert Imagination die Bedeutung von Erfahrung?",
    # #     "ground_truth": "Sie ermöglicht es, Erfahrungen innerlich zu rekonstruieren, zu kombinieren und neu zu deuten."
    # # },

    # # {
    # #     "question": "Warum ist ohne innere Modelle kein konzeptuelles Verständnis möglich?",
    # #     "ground_truth": "Weil Konzepte mentale Strukturen benötigen, die Relationen und Bedeutungen repräsentieren."
    # # },

    # # {
    # #     "question": "Wie trägt Imagination zur Entstehung neuer Einsichten bei?",
    # #     "ground_truth": "Durch das Hervorbringen neuer innerer Kombinationen, Perspektiven und hypothetischer Szenarien."
    # # },

    # # # -----------------------------------------------------
    # # # 51–60: Vier Aspekte des Lernens – Vertiefung
    # # # -----------------------------------------------------

    # # {
    # #     "question": "Warum können die vier Aspekte des verständnisintensiven Lernens nicht isoliert auftreten?",
    # #     "ground_truth": "Weil Verstehen erst durch ihr Zusammenspiel entsteht."
    # # },

    # # {
    # #     "question": "Wie hängt Erfahrung mit Metakognition zusammen?",
    # #     "ground_truth": "Erfahrungen werden erst durch Reflexion bewusst, bewertet und für künftiges Lernen nutzbar."
    # # },

    # # {
    # #     "question": "Warum ist Vorstellung ein vermittelndes Element zwischen Erfahrung und Begreifen?",
    # #     "ground_truth": "Weil Vorstellungen Erfahrungen innerlich zugänglich machen und Struktur für Begriffe schaffen."
    # # },

    # # {
    # #     "question": "Wie beschreibt der Text das Verhältnis von Begreifen und Regeln?",
    # #     "ground_truth": "Begreifen bedeutet Regeln zu entwickeln, zu prüfen und anzuwenden, nicht sie nur auswendig zu lernen."
    # # },

    # # {
    # #     "question": "Warum ist Metakognition ein zentraler Motor nachhaltigen Lernens?",
    # #     "ground_truth": "Sie ermöglicht bewusste Selbststeuerung und kritisches Überprüfen des eigenen Denkens."
    # # },

    # # {
    # #     "question": "Wie unterstützt Begreifen den Aufbau tragfähiger Wissensstrukturen?",
    # #     "ground_truth": "Durch logische Ordnung, Erkennen von Beziehungen und Ableiten allgemeiner Prinzipien."
    # # },

    # # {
    # #     "question": "Warum wird praktisches Lernen im Text als 'Ellipse' beschrieben?",
    # #     "ground_truth": "Weil es individuelles Tun und gesellschaftliche Tätigkeitsfelder verbindet."
    # # },

    # # {
    # #     "question": "Wie ergänzt Vorstellung die Lücke zwischen unmittelbarer Erfahrung und abstrakter Theorie?",
    # #     "ground_truth": "Sie transformiert Erfahrungen in symbolische, mentale Modelle, die Begriffe vorbereiten."
    # # },

    # # {
    # #     "question": "Warum ist Erfahrung sowohl aktiv als auch passiv?",
    # #     "ground_truth": "Aktiv durch Tun, passiv durch das Widerfahren von Ereignissen."
    # # },

    # # {
    # #     "question": "Wie trägt Metakognition zum Lernen des Lernens bei?",
    # #     "ground_truth": "Sie macht Lernprozesse selbst zum Gegenstand des Bewusstseins."
    # # },

    # # -----------------------------------------------------
    # # 61–70: Cross-Concept – Pädagogische Kritik, Rationalisierung, Bildung
    # # -----------------------------------------------------

    # {
    #     "question": "Warum bezeichnet der Text das moderne Schulsystem als 'systemrationalisiert'?",
    #     "ground_truth": "Weil es auf überprüfbare Fakten, Effizienz und kleinste Lerneinheiten fokussiert."
    # },

    # {
    #     "question": "Wie trägt Rationalisierung zur Vernachlässigung der Imagination bei?",
    #     "ground_truth": "Sie bevorzugt messbare Ergebnisse und verdrängt subjektive geistige Prozesse."
    # },

    # {
    #     "question": "Warum ist die Bedeutung des Zeichnens im historischen Kontext wichtig?",
    #     "ground_truth": "Weil Zeichnen als Form der Vorstellungsbildung anerkannt wurde, Imagination aber nicht."
    # },

    # {
    #     "question": "Warum führt Schulwissen oft nicht zu Bildung im humanistischen Sinne?",
    #     "ground_truth": "Weil Bildung Verknüpfung von Wissen, Handeln und Urteilen erfordert, nicht bloß Fakten."
    # },

    # {
    #     "question": "Wie erklärt der Text die Diskrepanz zwischen Wissenserwerb und Verstehen im modernen Unterricht?",
    #     "ground_truth": "Weil der Fokus auf Reproduktion statt auf innerer Modellbildung liegt."
    # },

    # {
    #     "question": "Warum bleibt faktenorientiertes Lernen häufig lebensfern?",
    #     "ground_truth": "Weil es Erfahrung und reale Anwendung kaum einbezieht."
    # },

    # {
    #     "question": "Wie unterstützt verständnisintensives Lernen eine mündige Bürgerschaft?",
    #     "ground_truth": "Weil es Selbstständigkeit, Verantwortlichkeit und kritische Urteilsfähigkeit fördert."
    # },

    # {
    #     "question": "Warum führt reine Informationsaufnahme nicht zu Kompetenz?",
    #     "ground_truth": "Weil Kompetenz Verstehen, Anwenden und Modellieren erfordert."
    # },

    # {
    #     "question": "Wie verbindet das Konzept Bildung Prozess und Ergebnis des Lernens?",
    #     "ground_truth": "Weil Bildung sowohl Lernhandeln als auch dessen Auswirkung umfasst."
    # },

    # {
    #     "question": "Warum wird der Begriff der Vorstellung erst spät wiederentdeckt?",
    #     "ground_truth": "Weil die Pädagogik lange unter dem Einfluss technischer Rationalität stand."
    # },

    # # -----------------------------------------------------
    # # 71–80: Anwendung in Coaching & Erwachsenenbildung
    # # -----------------------------------------------------

    # {
    #     "question": "Wie hilft Imagination Erwachsenen, schwierige Lebenssituationen neu zu interpretieren?",
    #     "ground_truth": "Indem sie alternative innere Bilder und Bedeutungen konstruiert."
    # },

    # {
    #     "question": "Warum ist erfahrungsbasiertes Lernen im Coaching effektiver als reine Analyse?",
    #     "ground_truth": "Weil Veränderungen durch gelebte Erfahrungen stärker im Verhalten verankert werden."
    # },

    # {
    #     "question": "Wie kann Metakognition Klienten helfen, destruktive Muster zu erkennen?",
    #     "ground_truth": "Durch bewusste Reflexion ihrer Denk- und Reaktionsweisen."
    # },

    # {
    #     "question": "Warum sind Modelle im Coaching entscheidend für Verhaltensänderung?",
    #     "ground_truth": "Weil Klienten innere Strukturen brauchen, um neue Handlungen mental vorzubereiten."
    # },

    # {
    #     "question": "Wie unterstützt das Konzept des verständnisintensiven Lernens nachhaltige Coaching-Prozesse?",
    #     "ground_truth": "Durch Integration von Erfahrung, Vorstellung, Begreifen und Reflexion."
    # },

    # {
    #     "question": "Warum scheitern viele Ratschläge, obwohl sie logisch sinnvoll sind?",
    #     "ground_truth": "Weil Klienten sie ohne innere Modellbildung nicht anwenden können."
    # },

    # {
    #     "question": "Wie ermöglicht Imagination emotionales Umlernen?",
    #     "ground_truth": "Durch das Erzeugen alternativer innerer Szenarien mit neuer Bedeutung."
    # },

    # {
    #     "question": "Warum ist reine Information im Coaching oft wirkungslos?",
    #     "ground_truth": "Weil sie keine innere Transformation auslöst."
    # },

    # {
    #     "question": "Wie hilft eine reflektierte Verbindung von Erfahrung und Vorstellung im Lerncoaching?",
    #     "ground_truth": "Sie ermöglicht tiefes Verständnis und handlungsfähige Kompetenz."
    # },

    # {
    #     "question": "Warum sollte Coaching immer Metakognition fördern?",
    #     "ground_truth": "Weil Klienten dadurch lernen, ihr Denken bewusst zu steuern."
    # },

    # # -----------------------------------------------------
    # # 81–90: Inference – Übertragung auf Problemlösung, Lernen, Kreativität
    # # -----------------------------------------------------

    # {
    #     "question": "Wie erklärt der Text die Rolle von Imagination bei kreativer Problemlösung?",
    #     "ground_truth": "Sie ermöglicht das Erzeugen neuer innerer Kombinationen, die zu innovativen Lösungen führen."
    # },

    # {
    #     "question": "Warum ist Verstehen ohne Metakognition instabil?",
    #     "ground_truth": "Weil fehlende Reflexion die Überprüfung und Sicherung von Einsicht verhindert."
    # },

    # {
    #     "question": "Wie lässt sich das Zusammenspiel der vier Lernaspekte als System verstehen?",
    #     "ground_truth": "Als dynamischer Prozess, in dem jeder Aspekt die anderen unterstützt und optimiert."
    # },

    # {
    #     "question": "Warum braucht tiefes Lernen immer auch emotionale Beteiligung?",
    #     "ground_truth": "Weil emotionale Relevanz die innere Modellbildung stärkt."
    # },

    # {
    #     "question": "Wie erklärt der Text den Unterschied zwischen Lernen und Verstehen?",
    #     "ground_truth": "Lernen kann oberflächlich sein, Verstehen verlangt Einsicht durch Erfahrung, Modelle und Reflexion."
    # },

    # {
    #     "question": "Warum ist es problematisch, Denken auf Logik zu reduzieren?",
    #     "ground_truth": "Weil Verstehen einen größeren Raum von Einsicht und Erfahrung umfasst."
    # },

    # {
    #     "question": "Wie hängen Hypothesenbildung und Vorstellung zusammen?",
    #     "ground_truth": "Hypothesen entstehen durch das innere Modellieren möglicher Zusammenhänge."
    # },

    # {
    #     "question": "Warum ist Experimentieren ein natürlicher Bestandteil verständnisintensiven Lernens?",
    #     "ground_truth": "Weil es Erfahrung, Modellüberprüfung und Reflexion verbindet."
    # },

    # {
    #     "question": "Warum kann ohne Erfahrung keine sinnvolle Metakognition stattfinden?",
    #     "ground_truth": "Reflexion braucht reale oder rekonstruierte Erlebnisse als Grundlage."
    # },

    # {
    #     "question": "Wie trägt die Verinnerlichung von Handlungserfahrungen zum Begreifen bei?",
    #     "ground_truth": "Sie bildet die Basis, auf der abstrakte Regeln entwickelt werden."
    # },

    # # -----------------------------------------------------
    # # 91–100: High-Level Cross-Concept & Coaching Transfer
    # # -----------------------------------------------------

    # {
    #     "question": "Wie lässt sich das pädagogische Konzept der inneren Wirklichkeit auf Selbstführung übertragen?",
    #     "ground_truth": "Durch bewusste Modellbildung, Reflexion und Nutzung innerer Bilder zur Steuerung eigenen Handelns."
    # },

    # {
    #     "question": "Warum benötigen Erwachsene im Coaching oft Re-Imagination alter Erfahrungen?",
    #     "ground_truth": "Weil festgefahrene Bedeutungen erst durch neue innere Bilder veränderbar sind."
    # },

    # {
    #     "question": "Wie erklärt der Text, dass Lernen ohne innere Beteiligung kaum transferiert wird?",
    #     "ground_truth": "Weil nur innerlich konstruiertes Wissen flexibel angewendet werden kann."
    # },

    # {
    #     "question": "Warum sind Fehler im verständnisintensiven Lernen wertvoll?",
    #     "ground_truth": "Weil sie Reflexion auslösen und zur Verbesserung von Modellen beitragen."
    # },

    # {
    #     "question": "Wie unterstützt Vorstellungsdenken die Fähigkeit, komplexe soziale Situationen zu verstehen?",
    #     "ground_truth": "Durch das mentale Simulieren von Perspektiven und Interaktionen."
    # },

    # {
    #     "question": "Warum ist das Zusammenspiel der vier Aspekte eine Voraussetzung für Expertise?",
    #     "ground_truth": "Weil Experten Erfahrung, Modelle, Begriffe und Reflexion integriert anwenden."
    # },

    # {
    #     "question": "Wie kann ein Coach Metakognition gezielt nutzen, um Widerstände aufzulösen?",
    #     "ground_truth": "Indem er Klienten ihre eigenen Denkprozesse bewusst macht."
    # },

    # {
    #     "question": "Wie verhindert verständnisintensives Lernen kognitive Überforderung?",
    #     "ground_truth": "Weil es Wissen an innere Modelle bindet und dadurch entlastet."
    # },

    # {
    #     "question": "Warum betont der Text, dass Verstehen ein Vernunftbezug ist?",
    #     "ground_truth": "Weil es Erfahrung, Einsicht und Urteilskraft zusammenführt."
    # },

    # {
    #     "question": "Wie ermöglicht das Konzept des Lernens als innere Wirklichkeit nachhaltige Transformation?",
    #     "ground_truth": "Durch aktive Modellbildung, bewusste Reflexion und sinnhaft integrierte Erfahrung."
    # }























]




# EVAL_DATA: list[dict[str, str]] = [
#     {
#         "question": "Who is Alice and what is her sister doing at the beginning of the story?",
#         "ground_truth": "Alice is a young girl who is feeling bored and sleepy. Her sister is sitting on the bank by her, reading a book, but Alice finds it uninteresting because it has no pictures or conversations."
#     },
#     {
#         "question": "What does the White Rabbit take out of its waistcoat-pocket?",
#         "ground_truth": "The White Rabbit takes a watch out of its waistcoat-pocket and looks at it before hurrying on."
#     }
#     ,
#     {
#         "question": "What is written on the bottle that Alice finds, and what happens when she drinks from it?",
#         "ground_truth": "The words 'DRINK ME' are beautifully printed on the bottle in large letters. After drinking it, Alice shrinks down to be only ten inches high."
#     },
#     {
#         "question": "Describe the character of the Caterpillar.",
#         "ground_truth": "The Caterpillar is a large, blue caterpillar found sitting on top of a mushroom, smoking a long hookah. It speaks in a sleepy, languid voice and gives Alice short, sometimes cryptic advice."
#     },
#     {
#         "question": "What is the capital of England?",
#         "ground_truth": "The story of Alice's Adventures in Wonderland does not contain information about the capital of England."
#     },
#     {
#         "question": "Why did the Mad Hatter and the March Hare put the Dormouse in the teapot?",
#         "ground_truth": "The story does not state a clear reason, but they attempt to put the Dormouse in the teapot after the Mad Hatter exclaims that the Dormouse is asleep again and wants to change the subject of conversation."
#     }
# ]
# "question": "What is the capital of England?",
# "ground_truth": "The story of Alice Adventures in Wonderland does not contain information about the capital of England."

# system prompt

# hidden prompts from llama-index