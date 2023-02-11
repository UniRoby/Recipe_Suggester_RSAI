import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;
import org.json.JSONArray;

public class RecipeReader {
    private String fileName;

    public RecipeReader(String fileName) {
        this.fileName = fileName;
    }

    public List<Recipe> getRecipes() {
        // Creiamo una lista vuota per contenere gli oggetti Recipe
        List<Recipe> recipes = new ArrayList<>();

        try {
            // Creiamo un oggetto CSVReader per leggere il file

            CSVReader reader = new CSVReader(new InputStreamReader(new FileInputStream(fileName), "ISO-8859-1"));

            // Leggiamo la prima riga (intestazione)
            String[] header = reader.readNext();

            // Leggiamo ogni riga successiva
            String[] line;
            while ((line = reader.readNext()) != null) {
                // Creiamo un nuovo oggetto Recipe per ogni riga
                Recipe recipe = new Recipe();
                recipe.setId(Integer.parseInt(line[0]));
                recipe.setTitle(line[1]);


                // Creiamo un oggetto JSONArray per estrarre gli ingredienti
                JSONArray ingredientsJson = new JSONArray(line[2]);

                // Creiamo un ArrayList<String> per contenere gli ingredienti
                ArrayList<String> ingredients = new ArrayList<>();

                // Aggiungiamo gli ingredienti all'ArrayList
                for (int i = 0; i < ingredientsJson.length(); i++) {
                    ingredients.add(ingredientsJson.getString(i));
                }


                recipe.setIngredients(ingredients);
                recipe.setLikes(Integer.parseInt(line[3]));
                recipe.setPrepTime(Integer.parseInt(line[4]));
                recipe.setCalories(Integer.parseInt(line[5]));

                // Aggiungiamo l'oggetto Recipe alla lista
                recipes.add(recipe);
            }

            // Chiudiamo il reader
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (CsvValidationException x) {
            x.printStackTrace();
        }
        return recipes;
    }




    public void printRecipes(List<Recipe> recipes) {
        // Stampa la lista di ricette
        for (Recipe recipe : recipes) {
            System.out.println(recipe);
        }
    }
}

