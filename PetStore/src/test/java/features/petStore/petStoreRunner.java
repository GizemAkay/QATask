package features.petStore;

import com.intuit.karate.junit5.Karate;

class petStoreRunner {
    
    @Karate.Test
    Karate testUsers() {
        return Karate.run("PetStore").relativeTo(getClass());
    }    

}
