package atelier_personne;
import java.time.LocalDate;
import java.util.ArrayList;

public class Secretaire extends Employe{
	
	private ArrayList<Manager> managerArray;
	
	protected Secretaire(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate dateEmbauche) {
		super(leNom ,lePrenom ,laDate ,lAdresse ,leSalaire ,dateEmbauche);
		this.managerArray = new ArrayList<Manager>(5);
	}
	
	public void setSalaire(double augmentation) {
		this.salaire = (this.salaire + (1+(0.1*augmentation))) * (1+(this.managerArray.size()*0.01));
	}
}
