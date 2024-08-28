package com.br.estudoscursoemvideo.idiomasistema;
import java.util.Locale;

public class IdiomaSistema {
    public static void main(String[] args) {
        Locale idioma = Locale.getDefault();
        
        System.out.print("Seu sistema esta em ");
        System.out.println(idioma.getDisplayLanguage()); // exibe "Português"
        System.out.println(idioma.getLanguage()); // exibe "pt"
    }
}
