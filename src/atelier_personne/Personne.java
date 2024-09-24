package atelier_personne;

import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Personne implements Cloneable{
    private static final Adresse ADRESSE_INCONNUE = null;
    private static int nbInstances = 0;
    private String nom;
    private String prenom;
    public final LocalDate dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
    
    
    //Constructors
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		nbInstances ++;
	}
	 
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'année de naissance
	 * @param numero le numero de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, LocalDate.of(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	
	//Methods Get and Set
	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le prénom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance
	 */
	public LocalDate getDateNaissance(){
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}
	
	/**
	 * Accesseur
	 * @return nbInstances
	 */
	public static int getNbInstances() {
		return nbInstances;
	}
	//Methods
	
	public static boolean evenPerson(Personne p1, Personne p2) {
		if(p1.dateNaissance.hashCode() == p2.dateNaissance.hashCode()) {
			return true;
		}
		return false;
	}
	
	public static boolean olderV1(Personne p1, Personne p2) {
		if(p1.dateNaissance.isBefore(p2.dateNaissance)){
			return true;
		}
		return false;
	}
	
	public boolean olderV2(Personne p2) {
		return (this.dateNaissance.compareTo(p2.dateNaissance) < 0);
	}
		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.format(DateTimeFormatter.ofPattern("dd-MM-yyyy"))+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}
	
	public boolean equals(Object obj) {
		boolean result = false;
		if ((obj != null) && (obj instanceof Personne)){
			Personne p2 = (Personne)obj;
			if(this.getNom() == p2.getNom() && this.getPrenom() == p2.getPrenom() && this.getDateNaissance() == p2.getDateNaissance() && this.getAdresse()) {
				result = true;
			}
		}
		return result;
	}
 
 }