# Expense Claim (Rozliczanie Wydatków i Delegacji)

Dokument **Expense Claim** pozwala pracownikom ubiegać się o zwrot kosztów poniesionych w celach służbowych (np. podróże służbowe, noclegi, paliwo, zakup materiałów biurowych) z poziomu interfejsu Frappe HR.

---

## 1. Wymagania wstępne (Prerequisites)
Przed utworzeniem rozliczenia w systemie wymagane są:
* Rekord pracownika (**Employee**).
* Typ wydatku (**Expense Claim Type**) z powiązanym domyślnym kontem księgowym.
* Rachunek rozliczeniowy pracownika (**Payable Account** / konto rozrachunków z pracownikami).
* Centrum kosztowe (**Cost Center**).
* Osoba weryfikująca (**Expense Approver**).

---

## 2. Ścieżka użytkownika krok po kroku (How to create)
1. Przejdź do: **HR > Expenses > Expense Claim > Add Expense Claim**.
2. Wybierz pracownika (**Employee**) – system uzupełni firmę oraz domyślnego akceptanta.
3. W tabeli **Expenses** dodaj pozycje wydatków:
   * Wybierz typ wydatku (**Expense Claim Type**).
   * Wprowadź datę wydatku (**Expense Date**).
   * Wpisz zgłaszaną kwotę (**Claimed Amount**).
   * Dodaj opis lub cel biznesowy wydatku.
4. **Załączniki**: Załącz skany paragonów, faktur lub biletów za pomocą bocznego panelu załączników (*Attachments*).
5. Jeśli na poczet wydatków pobrano wcześniej zaliczkę, powiąż ją w sekcji **Advances** (*Advance Paid*).
6. Kliknij **Save** (wersja robocza) lub **Submit** (przekazanie do akceptacji).

---

## 3. Kluczowe funkcje i ścieżka finansowa (Key Features)
* **Korekta kwoty przez akceptanta**: Przełożony może zmienić zatwierdzaną kwotę w kolumnie **Sanctioned Amount**, jeśli część wydatku nie kwalifikuje się do zwrotu zgodnie z polityką firmy.
* **Rozliczenie zaliczek (Advance Offset)**: System automatycznie pomniejsza kwotę do wypłaty pracownikowi o kwotę uprzednio pobranej zaliczki służbowej.
* **Integracja z listą płac lub księgowością**: Zatwierdzony wydatek może zostać zwrócony bezpośrednio w kolejnym pasku płacowym (*Include in Next Salary*) lub poprzez dedykowany przelew bankowy (*Payment Entry*).

---

## 4. Ostrzeżenia i walidacje systemowe (Notes & Warnings)

> [!WARNING]
> **Limit kwoty akceptowanej**: Wartość w polu *Sanctioned Amount* nie może być wyższa niż pierwotnie zgłoszona kwota w *Claimed Amount*.

> [!WARNING]
> **Wymóg konta księgowego**: Zgłoszenie nie może zostać zaksięgowane ani zatwierdzone finansowo, jeśli dla wybranego typu wydatku nie zdefiniowano konta kosztowego powiązanego z firmą pracownika.

> [!NOTE]
> **Blokada wypłaty przed pełną akceptacją**: Wygenerowanie dokumentu płatności (*Payment Entry*) jest możliwe wyłącznie po przejściu dokumentu w status *Approved* (zaakceptowany przez Expense Approver) oraz *Submitted*.
