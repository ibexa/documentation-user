# Ibexa DXP User Documentation

This repository is the source for [User Documentation for Ibexa DXP](https://doc.ibexa.co/projects/userguide/en/latest/),
a digital experience platform that is based on the Symfony Full Stack Framework in PHP.

# Resources

1. Ibexa DXP Developer Hub: https://developers.ibexa.co
1. Ibexa DXP Repository: https://github.com/ibexa/oss
1. Open JIRA board: https://issues.ibexa.co
1. Ibexa Website: https://ibexa.co
1. User Documentation: https://doc.ibexa.co/projects/userguide

## How to contribute

To contribute to the documentation, you can open a PR in this repository.

If you'd like to see Ibexa DXP in your language, you can [contribute to the translations](https://doc.ibexa.co/en/latest/resources/contributing/contribute_translations/).

## Build and preview documentation

To build and preview your changes locally, you need to install Python along with its package manager (`pip`).
To install other required tools, use the following command:

```bash
pip install -r requirements.txt
```

Then you can run:

```bash
mkdocs serve
```

After a short while your documentation should be reachable at http://localhost:8000.
If it's not, check the output of the command.

## Checking links

External links in the built documentation are checked using [lychee](https://lychee.cli.rs).

### Running the link checker

```bash
# 1. Build the main docs site
mkdocs build --strict

# 2. Clone and build versioned repositories, and generate lychee.toml
./tools/clone-repositories.sh

# 3. Check links
lychee --config lychee.toml --cache --cache-exclude-status "400.." site
```

After fixing any reported links, run `mkdocs build --strict` before rerunning `lychee`.

#### Using non-standard branches

The script accepts optional branch names before cloning repositories:

```bash
./tools/clone-repositories.sh [DEVDOC_50] [DEVDOC_46] [USERDOC_50] [USERDOC_46] [CONNECT]
```

| Argument     | Repository                      | Default |
|--------------|---------------------------------|---------|
| `DEVDOC_50`  | `ibexa/documentation-developer` | `5.0`   |
| `DEVDOC_46`  | `ibexa/documentation-developer` | `4.6`   |
| `USERDOC_50` | `ibexa/documentation-user`      | `5.0`   |
| `USERDOC_46` | `ibexa/documentation-user`      | `4.6`   |
| `CONNECT`    | `ibexa/documentation-connect`   | `main`  |

Example — checking link for release PRs:

```bash
./tools/clone-repositories.sh release-5.0.10 release-4.6.70 4.6 4.6 main
```

The same parameters are available as inputs when triggering the GitHub Actions workflow manually.

## Where to View

https://doc.ibexa.co
