// Programa para mostrar DATA e HORA atuais do sistema

package com.br.estudoscursoemvideo.horadosistema;
import java.util.Date;

public class HoraDoSistema {

    public static void main(String[] args) {
        Date relogio = new Date(); // Date variável = new Date();
        
        System.out.println("A hora do sistema eh " + relogio.toString());
    }
}

