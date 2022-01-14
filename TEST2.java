import java.util.*;


public class ZAD1{
    public static class Kandydet implements Comparable<Kandydet>,Cloneable
    {
        private String nazwa;
        private int wiek;
        private String wykształcony;
        private int latadoświadczenia;
        public Kandydet(String nazwa,int wiek,String wykształcony,int latadoświadczenia)
        {
            this.nazwa = nazwa;
            this.wiek = wiek;
            this.wykształcony = wykształcony;
            this.latadoświadczenia = latadoświadczenia;
        }

        public String getnazwa(){return this.nazwa;}
        public int getwiek(){return this.wiek;}
        public String getwykształcony(){return this.wykształcony;}
        public int getlatadoświadczenia(){return this.latadoświadczenia;}
        public int compareTo(Kandydet other)
        {
            return this.nazwa.compareTo(other.nazwa)+Integer.compare(this.wiek,other.wiek)+Integer.compare(this.wiek,other.wiek);
        }
        
    
    }
    public static class Rekrutacja
    {
        static int doświadczenie;
        public static int set()
        {doświadczenie=2;
        return doświadczenie;}
    }
    public static boolean  Qualified(Kandydet k)
    {
        if(k.getlatadoświadczenia()>=Rekrutacja.set())
        return true;
        else
        return false;
    }
    
    public static HashMap<Integer,String> RecruitmentMap(ArrayList<Kandydet> klist)
    {
        HashMap<Integer, String> mapa = new HashMap<Integer, String>();
        for(int i=0;i<klist.size();i++)
        {
            if(Qualified(klist.get(i))==true)
            mapa.put(klist.get(i).getlatadoświadczenia(),klist.get(i).getnazwa());
        }
        return mapa;
    }
   
    public static void main(String[] args) { 
        ArrayList<Kandydet> grupa = new ArrayList<Kandydet>();
        grupa.add(new Kandydet("Kowalski", 35, "licencjat", 1));
        grupa.add(new Kandydet("Zych", 34, "magistrat", 2));
        grupa.add(new Kandydet("Klops", 33, "magistrat", 3));
        grupa.add(new Kandydet("Jech", 32, "magistrat", 4));
        grupa.add(new Kandydet("Kek", 31, "magistrat", 5));
        grupa.add(new Kandydet("Górny", 30, "magistrat", 6));
        for(int i=0;i<grupa.size();i++)
        System.out.print(grupa.get(i).getnazwa()+" "+grupa.get(i).getwiek()+" "+grupa.get(i).getwykształcony()+" "+grupa.get(i).getlatadoświadczenia()+"\n");
        System.out.print("\n");
        Collections.sort(grupa);
        for(int i=0;i<grupa.size();i++)
        System.out.print(grupa.get(i).getnazwa()+" "+grupa.get(i).getwiek()+" "+grupa.get(i).getwykształcony()+" "+grupa.get(i).getlatadoświadczenia()+"\n");
        Kandydet test = new Kandydet("Klej", 30, "magistrat",  1);
        System.out.print(Qualified(test)+"\n");
        System.out.print(RecruitmentMap(grupa));
    }  
        

}
