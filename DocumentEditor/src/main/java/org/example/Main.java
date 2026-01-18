package org.example;

import org.example.Persistence.Persistence;
import org.example.Persistence.impl.Sout;

public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        Document document = new Document();
        Persistence sout = new Sout();
        DocumentEditor documentEditor = new DocumentEditor(document, sout);
        documentEditor.addText("hi");
        documentEditor.addNewLine();
        documentEditor.addImage("bac.jpeg");
        documentEditor.addNewLine();
        documentEditor.addText("the end");

        documentEditor.save();
    }
}