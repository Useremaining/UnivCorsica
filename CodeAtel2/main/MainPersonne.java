package main;
import java.time.LocalDate;
import java.util.ArrayList;
import atelier_personne.*;

public class MainPersonne {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Employe> arrayEmploye = new ArrayList<>();
		
		Employe e1 = Employe.createWorker("Jojo","jojo",LocalDate.of(2000,01,01),new Adresse(50,"rue du truc","20200","Bastia"),2000,LocalDate.of(2000,9,20));
		Employe e2 = Employe.createWorker("Jaja","jaja",LocalDate.of(1990,01,01),new Adresse(20,"rue du truc","20100","Bastia"),2000,LocalDate.of(2000,9,20));
		arrayEmploye.add(e1);
		
		for(int i=0; i<arrayEmploye.size();i++) {
			arrayEmploye[i].salaire * 1.1;
		}
	}

}
