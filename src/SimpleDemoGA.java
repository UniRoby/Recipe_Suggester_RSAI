import java.util.*;

import static org.apache.commons.lang3.BooleanUtils.or;

/**
 *
 * @author Roberto
 */

//Main class modifica2
public class SimpleDemoGA {

    Population population = new Population();
    Individual fittest;
    Individual secondFittest;
    int generationCount = 0;

//commento
    public static void main(String[] args) {

        RecipeReader reader= new RecipeReader("src\\recipes.csv");
        List<Recipe> recipes= reader.getRecipes();
        System.out.println("Size dataset: " +recipes.size());
        /*List<String> ingredients= new ArrayList<>();
        ingredients.add("farina");
        ingredients.add("acqua");
        ingredients.add("sale");
        ingredients.add("pomodoro");
        ingredients.add("mozzarella");
        ingredients.add("basilico");
        ingredients.add("gnocchi");*/

        Scanner sc = new Scanner(System.in);
        System.out.println("Inserisci gli ingredienti separati da virgole o spazi: ");
        String input = sc.nextLine();

        input = input.replaceAll(",\\s+", ",");
        // Crea l'array di stringhe
        String[] array = input.split("[,]+");

        // Crea la lista di stringhe
        List<String> ingredients = new ArrayList<String>(Arrays.asList(array));


        Random rn = new Random();

        SimpleDemoGA demo = new SimpleDemoGA();

        //set population size
        demo.population.setPopSize(20);
        //Initialize population
        demo.population.initializePopulation();

        //Calculate fitness of each individual
        demo.population.calculateFitness(recipes,ingredients);

        System.out.println("Generation: " + demo.generationCount + " Fittest: " + demo.population.fittest+", Nome ricetta: "+demo.population.getFittest().getRecipeTitle(recipes));
        //demo.population.printPopulation(recipes);

        //While population gets an individual with maximum fitness
        int iteration=0;
        boolean itera=true;
        while (demo.population.fittest < 40  & demo.generationCount <4) {

            ++demo.generationCount;

            //Do selection
            demo.selection();

            //System.out.println("\nindividuo 1 selezionato: " + demo.fittest.getRecipeTitle(recipes));
            //System.out.println("\nindividuo 2 selezionato: " + demo.secondFittest.getRecipeTitle(recipes));
            //Do crossover
            demo.crossover();
           // System.out.println("\nindividuo 1 post crossover: " + demo.fittest.getRecipeTitle(recipes));
            //System.out.println("\nindividuo 2 post crossover: " + demo.secondFittest.getRecipeTitle(recipes));

            // System.out.println("\nl'individuo 1 esiste?: "+demo.population.alreadyExists(demo.fittest,recipes));
            // System.out.println("\nl'individuo 2 esiste?: "+demo.population.alreadyExists(demo.secondFittest,recipes));
            if(demo.population.alreadyExists(demo.fittest,recipes) ||  demo.population.alreadyExists(demo.secondFittest,recipes)){
                // if(demo.population.alreadyExists(demo.fittest,recipes))
                // System.out.println("\nl'individuo 1 esiste già");
                // if(demo.population.alreadyExists(demo.secondFittest,recipes))
                //  System.out.println("\nl'individuo 2 esiste già");
                demo.mutation(recipes);
                // System.out.println("\nindividuo 1 post mutazione obbligatoria: " + demo.fittest.getRecipeTitle(recipes));
                // System.out.println("\nindividuo 2 post mutazione obbligatoria: " + demo.secondFittest.getRecipeTitle(recipes));
            }
            //Do mutation under a random probability
            /*if (rn.nextInt()%7 < 5) {
                demo.mutation();
                System.out.println("\nindividuo 1 post mutazione: " + demo.fittest.getRecipeTitle(recipes));
                System.out.println("\nindividuo 2 post mutazione: " + demo.secondFittest.getRecipeTitle(recipes));
            }*/
            // System.out.println("\nindividuo 1 ultimate: " + demo.fittest.getRecipeTitle(recipes));
            //System.out.println("\nindividuo 2 ultimate: " + demo.secondFittest.getRecipeTitle(recipes));

            //Add fittest offspring to population
            demo.addFittestOffspring(recipes,ingredients);

            //Calculate new fitness value
            demo.population.calculateFitness(recipes,ingredients);

            System.out.println("Generation: " + demo.generationCount + " Fittest: " + demo.population.fittest+", Nome ricetta: "+demo.population.getFittest().getRecipeTitle(recipes));
            //demo.population.printPopulation(recipes);

        }
        /*System.out.println("\ningredienti inseriti:  " );
        for(int i=0;i< ingredients.size();i++)
            System.out.println(ingredients.get(i));*/

        System.out.println("\nSoluzione trovata nella generazione " + demo.generationCount);
        System.out.println("Fitness: "+demo.population.getFittest().fitness);
        demo.population.printPopulation(recipes);
        System.out.print("\nRicetta più adatta: "+demo.population.getFittest().getRecipeTitle(recipes));
        System.out.print("\ningredienti: "+recipes.get(demo.population.getFittest().individual2Decimal()).getIngredients());
        System.out.print("\nAltra ricetta: "+demo.population.getSecondFittest().getRecipeTitle(recipes));
        System.out.print("\ningredienti: "+recipes.get(demo.population.getSecondFittest().individual2Decimal()).getIngredients());
        /*for (int i = 0; i < 8; i++) {
            System.out.print(demo.population.getFittest().genes[i]);
        }*/

        System.out.println("");

    }

    //Selection
    void selection() {

        //Select the most fittest individual
        fittest = population.getFittest().clone();

        //Select the second most fittest individual
        secondFittest = population.getSecondFittest().clone();
    }

    //Crossover
    void crossover() {
        Random rn = new Random();

        //Select a random crossover point

        int crossOverPoint = rn.nextInt(population.individuals[0].geneLength);

        //System.out.println("\nRandom point del crossover: "+crossOverPoint);
            //Swap values among parents
            for (int i = 0; i < crossOverPoint; i++) {
                int temp = fittest.genes[i];
                fittest.genes[i] = secondFittest.genes[i];
                secondFittest.genes[i] = temp;
            }

    }

    //Mutation
    void mutation(List<Recipe> recipes) {
        Random rn = new Random();

        //Select a random mutation point
        int mutationPoint = 0;
     do{
         mutationPoint=rn.nextInt(population.individuals[0].geneLength);
         //Flip values at the mutation point
         if (fittest.genes[mutationPoint] == 0) {
             fittest.genes[mutationPoint] = 1;
         } else {
             fittest.genes[mutationPoint] = 0;
         }
     }
     while(population.alreadyExists(fittest,recipes));

     do{
        mutationPoint = rn.nextInt(population.individuals[0].geneLength);

        if (secondFittest.genes[mutationPoint] == 0) {
            secondFittest.genes[mutationPoint] = 1;
        } else {
            secondFittest.genes[mutationPoint] = 0;
        }
     }
     while(population.alreadyExists(secondFittest,recipes));
    }

    //Get fittest offspring
    Individual getFittestOffspring() {
        if (fittest.fitness > secondFittest.fitness) {
            return fittest;
        }
        return secondFittest;
    }


    //Replace least fittest individual from most fittest offspring
    void addFittestOffspring(List<Recipe> recipes, List<String> ingredients) {

        //Update fitness values of offspring
        fittest.calcFitness(recipes,ingredients);
        secondFittest.calcFitness(recipes,ingredients);


        //Get index of least fit individual
        int leastFittestIndex = population.getLeastFittestIndex();
        //System.out.println("\nStampa del peggiore individuo della popolazione "+ population.individuals[leastFittestIndex].getRecipeTitle(recipes));
        //System.out.println("\nStampa del miglior individuo creato post crossover e mutazione: "+getFittestOffspring().getRecipeTitle(recipes));
        //Replace least fittest individual from most fittest offspring
        population.individuals[leastFittestIndex] = getFittestOffspring();
        //population.printPopulation(recipes);

    }

   /* void whatDoYouNeed(Recipe recipe, List<String> ingredients){

       for(i=0;i<)

    }*/

}


//Individual class
class Individual implements Cloneable {

    float fitness = 0;
    int[] genes = new int[8];
    int geneLength = 8;

    public Individual() {
        Random rn = new Random();

        //Set genes randomly for each individual
        for (int i = 0; i < genes.length; i++) {
            genes[i] = Math.abs(rn.nextInt() % 2);
        }

        fitness = 0;
    }

    public int individual2Decimal(){
        StringBuilder  s= new StringBuilder();
        for (int i : genes){
            s.append(i); //add all the ints to a string
        }
        int num=Integer.parseInt(s.toString(),2);

        return num;
    }

    public String getRecipeTitle(List<Recipe> recipes){
        int num=individual2Decimal();
        String error= "Individuo Non collegato a nessuna Ricetta";
        if(recipes.size()<num){
            System.out.println("dimensione recipes: "+recipes.size()+ " taglia num individuo: "+num);
            return error;
        }

        else
           return recipes.get(num).getTitle();

    }


    //Calculate fitness
    public void calcFitness(List<Recipe> recipes, List<String> ingredients) {

        fitness = 0;

        int ind=individual2Decimal();

        if(recipes.size()<ind)
            fitness=0;
        else {
            for(String ing : ingredients) //controlla per ogni ing della lista ingredients scelta dall'utente se è presente nella lista degli ingredienti della ricetta avente come indice l'individuo
            {
                for(int i=0; i<recipes.get(ind).getIngredients().size();i++){
                    if(recipes.get(ind).getSingleIngredient(i).equals(ing))
                        ++fitness;
                }
            }
            fitness= (fitness * recipes.get(ind).getLikes()) / recipes.get(ind).getPrepTime();
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Individual that = (Individual) o;
        return Float.compare(that.fitness, fitness) == 0 && geneLength == that.geneLength && Arrays.equals(genes, that.genes);
    }

    public Individual clone() {
        try {
            // chiamiamo il metodo clone() della superclasse per creare una copia superficiale
            Individual clone = (Individual) super.clone();

            // creiamo una copia profonda dell'array genes
            clone.genes = genes.clone();

            return clone;
        } catch (CloneNotSupportedException e) {
            // non dovrebbe mai accadere perché la classe implementa Cloneable
            return null;
        }
    }


}

//Population class
class Population {

    int popSize;
    Individual[] individuals;
    float fittest = 0;
    public Population() {}

    public Population(int size){
        this.popSize=size;
        this.individuals= new Individual[popSize];
    }

    public void setPopSize(int n){
        this.popSize=n;
        this.individuals= new Individual[popSize];
    }
    //Initialize population
    public void initializePopulation() {
        for (int i = 0; i < individuals.length; i++) {
            individuals[i] = new Individual();
        }
    }

    //Get the fittest individual
    public Individual getFittest() {
        float maxFit = Integer.MIN_VALUE;
        int maxFitIndex = 0;

        for (int i = 0; i < individuals.length; i++) {
            if (maxFit <= individuals[i].fitness) {
                maxFit = individuals[i].fitness;
                maxFitIndex = i;
            }
        }
        fittest = individuals[maxFitIndex].fitness;
        return individuals[maxFitIndex];
    }

    //Get the second most fittest individual
    public Individual getSecondFittest() {

        int maxFit1=0;
        int maxFit2=0 ;
        int i = 0;
        if(individuals[0].equals(getFittest())){
            maxFit1 = 1;
            maxFit2 = 1;
        }



        for (i=0; i < individuals.length; i++) {
            if (individuals[i].fitness > individuals[maxFit1].fitness) {
                maxFit2 = maxFit1;
                maxFit1 = i;
            } else if (individuals[i].fitness > individuals[maxFit2].fitness) {
                maxFit2 = i;
            }
            //System.out.println("\nSecond fittest: "+individuals[maxFit2].fitness);
        }

        return individuals[maxFit2];
    }

    //Get index of least fittest individual
    public int getLeastFittestIndex() {
        float minFitVal = Integer.MAX_VALUE;
        int minFitIndex = 0;
        for (int i = 0; i < individuals.length; i++) {
            if (minFitVal >= individuals[i].fitness) {
                minFitVal = individuals[i].fitness;
                minFitIndex = i;
            }
        }
        return minFitIndex;
    }

    //Calculate fitness of each individual
    public void calculateFitness(List<Recipe> recipes, List<String> ingredients) {

        for (int i = 0; i < individuals.length; i++) {
            individuals[i].calcFitness(recipes,ingredients);
        }
        getFittest();
    }

    public boolean alreadyExists(Individual ind ,List<Recipe> recipes){

        for (int i = 0; i < individuals.length; i++) {

            if(individuals[i].getRecipeTitle(recipes).equals(ind.getRecipeTitle(recipes)))
                return true;
        }
        return false;
    }

    public void printPopulation(List<Recipe> recipes){
        int numInd;
        for (int i = 0; i < individuals.length; i++) {
            numInd=i+1;
           System.out.println("Individuo "+numInd + " :"+individuals[i].getRecipeTitle(recipes) + ". Fintness: "+individuals[i].fitness);
        }
    }
}