# Leave Application (Wnioski Urlopowe)

Dokument **Leave Application** służy do składania i procesowania wniosków urlopowych przez pracowników w systemie Frappe HR. Umożliwia zautomatyzowane sprawdzanie dostępnego limitu dni, uwzględnianie kalendarza świąt oraz formalną ścieżkę akceptacji przez przełożonego.

---

## 1. Wymagania wstępne (Prerequisites)
Przed złożeniem wniosku w systemie muszą być zdefiniowane:
* Rekord pracownika (**Employee**) ze statusem *Active*.
* Typ urlopu (**Leave Type**) – np. urlop wypoczynkowy, chorobowy, bezpłatny.
* Przydział urlopu (**Leave Allocation**) – aktywny bilans dni na dany okres rozliczeniowy.
* Kalendarz dni wolnych (**Holiday List**) przypisany do pracownika lub firmy.
* Wyznaczona osoba akceptująca (**Leave Approver**).

---

## 2. Ścieżka użytkownika krok po kroku (How to create)
1. Przejdź do: **HR > Leaves > Leave Application > Add Leave Application**.
2. Wybierz pracownika (**Employee**) – system automatycznie zaczyta przypisanego akceptanta (**Leave Approver**) oraz firmę.
3. Wybierz typ urlopu (**Leave Type**). System wyświetli bieżący stan dostępnych dni (*Leave Balance*).
4. Wskaż ramy czasowe:
   * **From Date** – data początkowa.
   * **To Date** – data końcowa.
5. Jeśli wniosek dotyczy części dnia, zaznacz **Half Day** i wskaż datę połówkową oraz porę (pierwsza/druga połowa dnia).
6. Uzupełnij uzasadnienie (**Reason**) i w razie potrzeby wskaż pracownika zastępującego (**Employee Transfer / Substitute**).
7. Zapisz jako wersję roboczą (**Save**) lub wyślij do akceptacji (**Submit**).

---

## 3. Kluczowe funkcje i automatyzacje (Key Features)
* **Kalkulacja dni roboczych**: System automatycznie pomija weekendy i dni ustawowo wolne z przypisanej listy świąt (*Holiday List*), chyba że typ urlopu ma włączoną flagę wliczania świąt.
* **Obsługa wniosków wstecznych**: Możliwość aplikowania za okresy przeszłe (np. nagłe zwolnienie lekarskie), o ile nie blokuje tego polityka kadrowa.
* **Powiadomienia e-mail**: Automatyczna wysyłka powiadomienia do akceptanta w momencie zatwierdzenia wniosku przez pracownika.

---

## 4. Ostrzeżenia i walidacje systemowe (Notes & Warnings)

> [!WARNING]
> **Nakładanie się terminów (Overlapping Leaves)**: System bezwzględnie blokuje zatwierdzenie wniosku, jeśli wskazany zakres dat pokrywa się z innym, wcześniej złożonym lub zaakceptowanym wnioskiem danego pracownika.

> [!WARNING]
> **Niewystarczający bilans (Insufficient Balance)**: Jeżeli wnioskowana liczba dni przekracza stan w *Leave Allocation*, system uniemożliwi wysłanie wniosku, chyba że w konfiguracji danego typu urlopu zaznaczono opcję *Allow Negative Balance*.

> [!NOTE]
> **Zasada blokady edycji**: Po kliknięciu **Submit** wniosek przechodzi w status *Open/Applied* i pracownik nie może już go modyfikować. Wszelkie korekty wymagają odrzucenia (*Reject*) lub anulowania (*Cancel*) dokumentu przez przełożonego lub administratora HR.
