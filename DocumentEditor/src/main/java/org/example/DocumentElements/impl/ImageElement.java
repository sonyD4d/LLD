package org.example.DocumentElements.impl;

import org.example.DocumentElements.DocumentElement;

public class ImageElement implements DocumentElement {
    private final String path;
    public ImageElement(String path) {
        this.path = path;
    }

    @Override
    public String render() {
        return "[Image : " + this.path + "]";
    }
}
