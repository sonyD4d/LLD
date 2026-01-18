package org.example;

import org.example.DocumentElements.DocumentElement;

import java.util.ArrayList;
import java.util.List;

public class Document {
    private final List<DocumentElement> documentElementList = new ArrayList<>();

    public void addDocumentElementInterface(DocumentElement documentElement) {
        this.documentElementList.add(documentElement);
    }

    public String render() {
        StringBuilder result = new StringBuilder();
        for(DocumentElement documentElement : this.documentElementList) {
            result.append(documentElement.render());
        }
        return result.toString();
    }
}
