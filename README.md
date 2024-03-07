# HeNN eLibrary Deployments

## 👋 hello

This is a database of eLibrary deployments done under [Help Nepal Network](https://helpnepal.net/) in different parts of Nepal.

With the goal of Help Nepal Network to provide support in the sectors of health and education in rural Nepal, it is running an e-library project with the slogan **“One e-library per district”**.

E-library or electronic library is an ambitious and innovative project launched by Help Nepal Network to offer computer facilities for the benefit of students and communities in all 75 districts of the country. This low-cost, low-maintenance model is highly suitable for rural Nepal. But most importantly, for the first time in their lives, the Help Nepal e-Library will allow beneficiaries to leverage modern information and communication technology (ICT) to enhance learning, build computer skills and narrow the digital divide.

## 💻 Setup

Create and activate virtual env

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

## 🔄 Converting eLibrary csv to html and markdown

```bash
cd scripts
python csv_to_table.py
```

## 🗒️ TODO

- [ ] Create script to auto populate geojson

## License

[MIT](LICENSE)
