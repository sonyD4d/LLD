package org.example.Persistence.impl;

import org.example.Persistence.Persistence;

public class Sout implements Persistence {
    @Override
    public void save(String text) {
        System.out.println(text);
    }
}
