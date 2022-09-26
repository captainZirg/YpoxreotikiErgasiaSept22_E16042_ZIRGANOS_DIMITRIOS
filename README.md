# YpoxreotikiErgasiaSept22_E16042_ZIRGANOS_DIMITRIOS

# Προϋποθέσεις προγράμματος
Για την λειτουργία του προγράμματος εγκαθιστούμε την Python και τις βιβλιοθήκες
Pymongo json flask
Δημιουργουμε ενα docker image συνδεδεμενο με ενα container της MONGODB και βάζουμε την βάση δεδομένων DSAirlines με collections users,reservations,flights.
Για να τρέξει το πρόγραμμα χρησιμοποιούμε το Pycharm

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


![image](https://user-images.githubusercontent.com/105843945/192243088-5fc58919-3fe4-4c00-b72a-aa21bce82ed4.png)

![image](https://user-images.githubusercontent.com/105843945/192243374-e3cfde1a-76a9-49dc-a33b-573d5565e9b1.png)





