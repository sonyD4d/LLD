package org.example.DocumentElements.impl;

import org.example.DocumentElements.DocumentElement;

public class NewLineElement implements DocumentElement {

    @Override
    public String render() {
        return "\n";
    }
}
