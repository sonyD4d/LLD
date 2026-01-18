package org.example;

import org.example.DocumentElements.impl.ImageElement;
import org.example.DocumentElements.impl.NewLineElement;
import org.example.DocumentElements.impl.TextElement;
import org.example.Persistence.Persistence;

public class DocumentEditor {
    private final Document document;
    private final Persistence persistence;

    public DocumentEditor(Document document, Persistence persistence) {
        this.document = document;
        this.persistence = persistence;
    }

    public void addText(String text) {
        this.document.addDocumentElementInterface(new TextElement(text));
    }

    public void addImage(String path) {
        this.document.addDocumentElementInterface(new ImageElement(path));
    }

    public void addNewLine() {
        this.document.addDocumentElementInterface(new NewLineElement());
    }

    public String render() {
        return this.document.render();
    }

    public void save() {
        persistence.save(render());
    }
}
