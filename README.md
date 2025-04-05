> [!NOTE]
> Development has moved to [https://github.com/louisdevie/komoe](https://github.com/louisdevie/komoe)

# Sass plugin for Komoe

# Installation

`pip install komoe-sass==0.1.0`

You will also need to [install the Sass compiler](https://sass-lang.com/install).

# Setup

Add the following to your `komoe.toml`:

```toml
[plugin.sass]
package = "komoe_sass"
config = { path = "style" } # the directory where to look for .scss and .sass files
```

---

*All the code in the repository belongs to the public domain*
