package atelier_personne;
import java.time.LocalDate;
import java.util.ArrayList;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Manager extends Employe{
	
	private Secretaire assignedSec;
	protected Manager(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate dateEmbauche, Secretaire s) {
		super(leNom ,lePrenom ,laDate ,lAdresse ,leSalaire ,dateEmbauche);
		this.assignedSec = s;
	}
	
	public void setSalaire(double augmentation) {
		this.salaire = (this.getSalaire()+ (1+(0.1*augmentation))) * (1+(annuityCalcul(this.getDateHired())*0.05));
	}
	
	public void setSecretaire(Secretaire s) {
		this.assignedSec = s;
	}
}
