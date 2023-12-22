# 🎁♾️ Generative AI-as-a-Service - Serverless Template 

This a fully functioning example project for serverless `Generative AI`-as-a-Service (aka `generative-ai-serverless`).

## Purpose

The project was originally built as a fun project to generate custom images with AI based on the interests of a particular person or organization then to give the recipient(s) a URL that they could access and hit refresh to get new fun and random images. Basically, `gen ai`-as-a-Gift where the recipient(s) have their own custom URL (using a URL shortener) to access and share without needing to know the details of the service and AI models.

When deployed, this project is a **self-contained scalable serverless environment for Generative AI** in AWS using API Gateway and AWS Lambda. While you are likely familiar with serverless web services, for the purposes of this project this means that you do not have to maintain servers and infrastructure. Amazon Web Services (AWS) handles horizontal scaling, and you only pay for the time and resources used (which is perfect for a project like this or many types of large scale services). In many cases, running this project and services within AWS will be completely free if you are within the free tier limits.

<p align="center">
	<img src="https://github.com/jgill333/generative-ai-serverless/assets/3399813/f0e509af-f866-47d2-b0c1-ec9c9db7827e" width="200">
	<img src="https://github.com/jgill333/generative-ai-serverless/assets/3399813/8eab6195-2c3d-47b8-9a9c-af32e8cd2525" width="200">
	<img src="https://github.com/jgill333/generative-ai-serverless/assets/3399813/af6ddaca-0272-4bdf-9ae7-51f2d6db4220" width="200">
</p>


#### Connect

[![LinkedIn][LinkedIn]][Linkedin-url]


### Pre-requisites

[![Python][Python]][python-url]

- 🐍 Python 3.11 or greater
- AWS CLI Profile (`access key` and `secret access key`)
- Stability AI API Key

### Setup Steps 

1. Clone this repository locally
2. Setup a `virtual environment` from the local directory that the repository was cloned into from the command-line: 
	```python
	$ python3 -m pip install virtualenv
	$ python3 -m virtualenv venv
	```

	Note: `virtual environments` may be created in a different way, depending on your `python` installation and configuration. For example, for some setups the `virtual environment` setup will look similar to this without a `python` version and using the `venv` package: 

	```python
	$ python -m venv venv
	```

3. Activate the `virtual environment` from within the directory of the local repository:
	```bash
	$ venv/bin/activate 
	# Note: The relative path to the activate script
	# may be at a location like the following: 
	# $ venv\scripts\activate 
	# Optionally, you may run one of the `activate` 
	# script helper files in the top-level directory
	# of the source for this repository. 
	# For example, on `windows` run `activate.bat` 
	# from the command-line (which this will do): 
	# > activate
	```

4. Get/set your API keys. Create a new accounts at `Stability AI` if you do not already have API credentials or a key(s).

```bash
$ export OPEN_AI_API_KEY=<open_ai_token>
$ export STABILITY_AI_API_KEY=<stability_ai_token>
```

5. Install the requirements needed to run the application locally with the following command from the same activated-`virtual environment` command-line window:
```bash
$ pip install -r requirements.txt
```

6. Run the local server from within the activated `virtual environment` with auto-reload on code changes:
```bash
$ flask --app main.py --debug run
```

7. Access the `debug` server locally by opening a URL in your web browser of choice at the route returned from the server run process, i.e. typically [`http://127.0.0.1:5000`](http://127.0.0.1:5000). You should see a `Hello!` response.

```bash
 * Serving Flask app 'main.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
 ```

 8. Generate images at the `/fun` route, e.g. [`http://127.0.0.1:5000/fun`](http://127.0.0.1:5000/fun). You may also customize the images by appending the `?prompt=<prompt modification>` querystring like [`http://127.0.0.1:5000/fun?prompt=flying cat in a futuristic city`](http://127.0.0.1:5000/fun?prompt=flying%20cat%20in%20a%20futuristic%20city).

### Deploy Steps

The following will create a serverless stack of an API Gateway, Lambda, etc. in AWS and give you a URL that is exeternally accessible. 

1. Run the following command (it will error if you do not have the AWS CLI configured locally) from an activated-`virtual environment` command-line window with a deployment configuration from `zappa_settings.py` (this project defaults to the configuration name of `gen-ai`). The configuration file uses the [`zappa settings format`](https://github.com/zappa/Zappa):

```bash
$ zappa deploy gen-ai
```
The command line output will look similar to the following as the service deploys: 
```bash
Deploying...
Your application is now live at: https://abc123.execute-api.us-east-1.amazonaws.com/gen-ai
```

**The URL that is provided as part of the deploy or update process is a publicly accessible URL that you may access, share, run, etc. 🎉**

2. If you make any changes to the service and wish to redeploy it (and replace all running instances) then run the following command from an activated-`virtual environment` command-line window
```bash
$ zappa update gen-ai
```

Note: To teardown the resources and stack and make the URL no longer accessible run:
```bash
$ zappa undeploy gen-ai
```

<!-- Markdown Reference Links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/Python-ffdf76?style=for-the-badge&logo=python&logoColor=#004d7a
[python-url]: https://www.python.org/
[LinkedIn]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=#ffffff
[linkedin-url]: https://www.linkedin.com/in/jonathangill1/