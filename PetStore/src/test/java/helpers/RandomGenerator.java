package helpers;

import org.apache.commons.lang.RandomStringUtils;

import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class RandomGenerator {
    public static void main(String[] args) {
        System.out.println(getNumber(11));
    }
    public static int getNumber() {
        Random random = new Random();
        StringBuilder string = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            int num = random.nextInt(10);
            string.append(num == 0 ? 1 : num);
        }
        return Integer.parseInt(String.valueOf(string));
    }

    public static Object getNumber(int count) {
        if (count > 10) {
            return (long) Math.floor(Math.random() * (Math.pow(10, count) - Math.pow(10, count-1) + 1)) + Math.pow(10, count-1);
        } else {
            return (int) Math.floor(Math.random() * (Math.pow(10, count) - Math.pow(10, count-1) + 1)) + Math.pow(10, count-1);
        }
    }

    public static String getGender(){
        Random random = new Random();
        List<String> genders = Arrays.asList("Female", "Male");
        return genders.get(random.nextInt(genders.size()));
    }

    public static String getName(){
        Random random = new Random();
        List<String> petNames = Arrays.asList("Fındık", "Karamel", "Pamuk", "Fütü", "Bihter", "Daisy", "Venüs", "Kont", "Ela", "YulafGaga");
        return petNames.get(random.nextInt(petNames.size()));
    }

}
