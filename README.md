# YpoxreotikiErgasiaSept22_E16042_ZIRGANOS_DIMITRIOS

# Προϋποθέσεις προγράμματος
Για την λειτουργία του προγράμματος εγκαθιστούμε την Python το MongoDB Compass το POSTMAN και τις βιβλιοθήκες
Pymongo json flask
Ανοίγουμε το MongoDB Compass και βάζουμε την βάση δεδομένων DSAirlines με collections users,reservations,flights.
Από τα αρχεία json users και flights βάζουμε όλα τα στοιχεία στα αντίστοιχα collections (users.json στο collection users flights.json στο collection flights.
Για να τρέξει το πρόγραμμα χρησιμοποιούμε το Pycharm
Δεν κατάφερα να χρησιμοποιήσω docker.

#Λειτουργία προγράμματος
Για να κάνουμε τα request χρησιμοποιούμε το POSTMAN με url http://127.0.0.1:5000/ και το app root της κάθε συνάρτησης. Για να εισάγουμε τα δεδομένα μας, πατάμε στο raw και συμπληρώνουμε τα στοιχεία

#Function create_user

![image](https://user-images.githubusercontent.com/105843945/192237233-9b621f88-33f3-43ca-b20a-58de2fef9d86.png)

Εισάγουμε τα απαραίτητα δεδομένα σε μορφή json.
Το πρόγραμμα ελέγχει εάν υπάρχει χρήστης με ίδιο πεδίο mail ή username ή passport.
Σε περίπτωση που δεν υπάρχει:
Εάν το password δεν είναι έγκυρο ή εάν το passport δεν είναι έγκυρο σύμφωνα με τις προϋποθέσεις της εργασίας τότε εμφανίζεται ανάλογο μήνυμα και δεν επιτρέπει στον χρήστη να δημιουργήσει account


Παράδειγμα εισαγωγής χρήστη

![image](https://user-images.githubusercontent.com/105843945/192238974-d5e3becb-663b-471a-9b9b-e43f63164b16.png)

![image](https://user-images.githubusercontent.com/105843945/192238598-cd44c0bc-b56f-47c8-a81e-9319c53b6760.png)

Παράδειγμα μη εισαγωγής χρήστη λόγω ίδιου πεδίου mail ή username

![image](https://user-images.githubusercontent.com/105843945/192238974-d5e3becb-663b-471a-9b9b-e43f63164b16.png)

![image](https://user-images.githubusercontent.com/105843945/192239334-e6d23442-cd0e-4255-a0ae-1509a1442ba8.png)

Παράδειγμα μη εισαγωγής χρήστη λόγω ακύρου πεδίου password

![image](https://user-images.githubusercontent.com/105843945/192239779-2043ebef-1349-42da-9d25-d518bac105be.png)

![image](https://user-images.githubusercontent.com/105843945/192239948-0801bae6-3233-4752-830f-f691e2ebd8e9.png)

Παράδειγμα μη εισαγωγής χρήστη λόγω ακύρου πεδίου passport

![image](https://user-images.githubusercontent.com/105843945/192241062-f084165d-f13e-41e1-9874-06c93b283568.png)

![image](https://user-images.githubusercontent.com/105843945/192241193-1ec7dcad-f289-44b4-99b9-614757e697d9.png)


#Function login
Εισάγουμε τα απαραίτητα δεδομένα.
Εάν το mail υπάρχει μέσα στην βάση τότε το πρόγραμμα ψάχνει να βρει εάν υπάρχει και το password.
Το πρόγραμμα ελέγχει την κατηγορία του user.Το output διαφέρει ανάλογα με αυτήν.
Εάν ο χρήστης ανήκει στην κατηγορία disabled τότε δεν μπορεί να κάνει login.
Σε περίπτωση που δεν εισάγει σωστά τα δεδομένα του εμφανίζεται και το ανάλογο μήνυμα

Παράδειγμα επιτυχημένου login

![image](https://user-images.githubusercontent.com/105843945/192243088-5fc58919-3fe4-4c00-b72a-aa21bce82ed4.png)

![image](https://user-images.githubusercontent.com/105843945/192243374-e3cfde1a-76a9-49dc-a33b-573d5565e9b1.png)

Παράδειγμα αποτυχημένου login


![image](https://user-images.githubusercontent.com/105843945/192250187-1748daf9-53b3-475e-8472-52d2de32efcf.png)

Παράδειγμα αποτυχημένου login λόγω disabled category


![image](https://user-images.githubusercontent.com/105843945/192250473-3179ace3-9ec8-4dad-a7b4-4743cd000fbb.png)


#Function disableThisUser
Ελέγχει αρχικά εάν τα δεδομένα είναι σωστά.
Σε περίπτωση που ο user είναι disabled στέλνει το απαραίτητο μήνυμα.
Διαφορετικά αλλάζει το category σε disabled και βάζει ένα recoveryPassword που του δίνει την δυνατότητα να αλλάξει το category ξανά σε user.
Το recoveryPassword επιλέγεται με τυχαίο τρόπο μέσα από χαρακτήρες και αριθμούς.

Παράδειγμα επιτυχημένου disableThisUser

![image](https://user-images.githubusercontent.com/105843945/192251956-f6e1881f-aea6-4981-a9f6-c3280017581f.png)


#Function enableThisUser
Ο χρήστης περνάει το διαβατήριο και το password που του δόθηκε κατά την disableThisUser.
Σε περίπτωση που είναι σωστό, τότε το category αλλάζει σε user.

Παράδειγμα επιτυχημένου enableThisUser

![image](https://user-images.githubusercontent.com/105843945/192252832-384b7e5a-2d23-4bdd-b337-f486872e6b92.png)


#Function createAdmin
Ελέγχει ότι ο χρήστης δεν είναι user.Έπειτα ελέγχει εάν το email που εισήγαγε ο admin υπάρχει ήδη στην βάση. Εάν δεν υπάρχει τότε δημιουργείται ένας νέος admin.


Παράδειγμα επιτυχημένου createAdmin


![image](https://user-images.githubusercontent.com/105843945/192254101-3e5879eb-cc07-4b19-b8bc-cd2593eb8a2e.png)


#Function insert flight
Αρχικά ελέγχει ότι ο χρήστης δεν είναι user. Σε περίπτωση που είναι δεν του επιτρέπεται η πρόσβαση. Εάν και μόνο αν είναι admin τότε μπορεί να εισάγει τα δεδομένα date,departure,destination,cost και duration.
Ο μοναδικός αριθμός πτήσης προκύπτει από τους πρώτους χαρακτήρες που ζητάει η εκφώνηση. Αυτό επιτυγχάνεται με την slice και μετά με την ένωση σε ένα string και την ανάθεση του ως flightID.

Παράδειγμα επιτυχημένου insert flight

![image](https://user-images.githubusercontent.com/105843945/192256119-c660a1c3-ce96-4e63-8f69-71d3a20d008c.png)


![image](https://user-images.githubusercontent.com/105843945/192256171-bbb44a95-5b13-4620-b827-0e0cff59d435.png)


#Function update flight

Αρχικά ελέγχει ότι ο χρήστης δεν είναι user. Έπειτα ψάχνει τις πτήσεις με το επιθυμητό flightID. Εάν βρει ελέγχει ότι η διαθεσιμότητα είναι 220. Μετά βάζει το επιθυμητό κόστος που ελέγχεται εάν είναι μεγαλύτερο του μηδέν.Τότε εισάγεται το νέο κόστος. Σε οποιαδήποτε άλλη περίπτωση στέλνονται τα ανάλογα μηνύματα.

Παράδειγμα επιτυχημένου update flight

![image](https://user-images.githubusercontent.com/105843945/192257416-a1de884e-c787-469c-b351-48e6422ac48e.png)

![image](https://user-images.githubusercontent.com/105843945/192257464-83fa8adc-6429-43cd-a5e6-44001ce3f6de.png)


#Function delete flight

Αρχικά ελέγχει ότι ο χρήστης δεν είναι user. Έπειτα ψάχνει βάσει του flightID την πτήση. Εάν υπάρχει την διαγράφει.

![image](https://user-images.githubusercontent.com/105843945/192257987-9e0318e6-6cd4-4373-9655-591bc8ca9ce0.png)
