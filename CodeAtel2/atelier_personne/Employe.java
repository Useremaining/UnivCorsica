package atelier_personne;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Employe extends Personne {
	
	//Attributes and variables
	
	private final LocalDate dateHired; 
	protected double salaire;
	private static final int AGE_MIN = 16;
	private static final int AGE_MAX = 67;
	
	//Constructors
	protected Employe(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate dateEmbauche) {
		super(leNom,lePrenom,laDate,lAdresse);
		dateHired = dateEmbauche;
		salaire = leSalaire;
	}
	
	protected Employe(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville, double leSalaire, int jHire, int mHire, int aHire) {
		this(leNom,lePrenom,LocalDate.of(a,m,j),new Adresse(numero,rue,code_postal,ville),leSalaire,LocalDate.of(aHire, mHire, aHire));
	}
	
	//Setter and Getter
	
	public double getSalaire() {
		return salaire;
	}

	public void setSalaire(double percent) {
		this.salaire = this.salaire * (1+(percent*0.1)) ;
	}

	public LocalDate getDateHired() {
		return dateHired;
	}

	public int getAGE_MIN() {
		return AGE_MIN;
	}

	public int getAGE_MAX() {
		return AGE_MAX;
	}
	
	//Methods
	
	public static Employe createWorker(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate dateEmbauche) {
		int annee = Period.between(laDate, LocalDate.now()).getYears();
		if(AGE_MIN >= annee || annee >= AGE_MAX) {
			return null;
		}
		return new Employe(leNom,lePrenom,laDate,lAdresse,leSalaire,dateEmbauche);
	}


	public void salaryRaising(float pourcent) {
		if( 0 < pourcent ){
			this.salaire = this.salaire * (1+(pourcent*0.1));
		}
	}
	
	/*public int annuityCalcul(LocalDate hiredDate) {
		LocalDate auj = LocalDate.now();
		int annuity = 0;
		if (Period.between(hiredDate, auj).getYears() == 0 && hiredDate.getYear() != auj.getYear()) {
			annuity ++; 
		}
		else if(Period.between(hiredDate, auj).getYears() > 0) {
			if(hiredDate.getMonthValue() > auj.getMonthValue()) {
				annuity += Period.between(hiredDate, auj).getYears() +1;
			}
			else {
				annuity += Period.between(hiredDate, auj).getYears();
			}
		}
		return annuity;
	}*/
	
	public int annuityCalcul(LocalDate hiredDate) {
		return Period.between(hiredDate, LocalDate.now()).getYears() + 1;
	}

}
