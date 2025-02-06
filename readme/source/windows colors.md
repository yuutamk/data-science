<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>


```code

```

</div>


Para lograr que el borde sea de color negro y que el fondo de la ventana se adapte al color del tema del navegador, puedes utilizar el atributo de `border` para el borde y las propiedades CSS `var()` para obtener los colores del tema del navegador (dark mode/light mode). Aquí tienes un ejemplo modificado:

```html
<div style="background: var(--background-color, #1E1E1E); padding: 10px; border: 2px solid black; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>

  <pre>
```code

```
  </pre>
</div>
```

Para que el fondo de la ventana se adapte al color del tema del navegador, asegúrate de definir las variables CSS `--background-color` según el modo oscuro o claro. Aquí tienes un ejemplo de cómo definir estas variables en tu CSS:

```css
:root {
  --background-color: #ffffff; /* Color de fondo para modo claro */
}

@media (prefers-color-scheme: dark) {
  :root {
    --background-color: #1E1E1E; /* Color de fondo para modo oscuro */
  }
}
```

De esta manera, el fondo de la ventana se adaptará automáticamente según el tema del navegador y el borde será de color negro. ¡Espero que esto te sea útil! 😊