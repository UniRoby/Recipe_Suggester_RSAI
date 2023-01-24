import java.util.ArrayList;
import java.util.Arrays;

public class Recipe {
    private int id;
    private String title;
    private ArrayList<String> ingredients;
    private int likes;
    private int prep_time;
    private int calories;

    public Recipe() {}
    public Recipe(int id, String title, ArrayList<String> ingredients, int likes, int prep_time, int calories) {
        this.id = id;
        this.title = title;
        this.ingredients = ingredients;
        this.likes = likes;
        this.prep_time = prep_time;
        this.calories = calories;
    }

    @Override
    public String toString() {
        return "Recipe{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", ingredients=" + ingredients +
                ", likes=" + likes +
                ", prep_time=" + prep_time +
                ", calories=" + calories +
                '}';
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public ArrayList<String> getIngredients() {
        return ingredients;
    }
    public String getSingleIngredient(int i){
        return ingredients.get(i);
    }

    public int getLikes() {
        return likes;
    }

    public int getPrepTime() {
        return prep_time;
    }

    public int getCalories() {
        return calories;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setIngredients(ArrayList<String> ingredients) {
        this.ingredients = ingredients;
    }

    public void setLikes(int likes) {
        this.likes = likes;
    }

    public void setPrepTime(int prep_time) {
        this.prep_time = prep_time;
    }

    public void setCalories(int calories) {
        this.calories = calories;
    }
}
