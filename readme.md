# Self-Hosted Codecov
> Code coverage done right.® Empower your developers with Codecov to improve code quality.

> We believe that everyone should have access to quality software (like Sentry), that’s why we have always offered Codecov for free to open source maintainers.
>
> By open sourcing Codecov, we’re not only joining the community that’s supported us from the start — but also want to make sure that every developer can contribute to and build on the Codecov experience.

Testing software is crucial for deploying healthy code. Codecov provides metrics and insight in the results of tests through code coverage reports. Coverage reports are used to determine what lines of code were tested and what lines were missed entirely. These reports are uploaded to Codecov to be analyzed and stored historically. This information helps your developers save time tracking down bugs and commit stronger code that is well tested, to increase code coverage to 100%.

### Features

Commit statuses and pull request comments are key to maintaining a healthy product. Codecov provides valuable metrics in the pull request feed and promotes healthy development.

Our unique Coverage Diff® will describe the commit in relation to its impact on tests which significantly improves code reviews.

### Usage

This repo is meant for a quick POC that can be ran locally. It is recommended to use Helm or Terraform to deploy Codecov in production.

Codecov currently requires your team to use one or more of the following: GitHub, GitHub Enterprise, GitLab, Gitlab CE, GitLab Enterprise, Bitbucket and Bitbucket Server. You will need to configure one (or more) of these providers for your self-hosted install of Codecov to function correctly. 

We recommend using our [Self-Hosted Configuration Guide](https://docs.codecov.com/docs/configuration) to ensure that your self-hosted install is properly configured.

### License Generation

Codecov self-hosted is based on Codecov's Enterprise On-Premises offering which is now deprecated. As a result, this software requires a license to run properly. **This is purely a technical requirement of the software at this time** and you will never be asked to purchase a license from Codecov or any other entity in order to use Codecov self-hosted. 

The installation comes with a general license with a 50 user seat limit. We chose 50 seats as we believe this is the maximum number of users a Docker Compose based PoC can reliably support out of the box, but your mileage may vary depending on how you plan to use Codecov. 

If you require more seats, a `license.py` script has been added that you can use from the command line to generate a license. From the scripts directory, run the following command:

```
python3 license.py new --expires=2030-12-25 --company=company-name  --users=50
```
You can set `expires`, `company`, and `users` to whatever future date, name, and user count you wish respectively, but those arguments are required for the script to function properly. 

Note that this script requires pycryptodome to be installed on your system. You can install it with:

```
pip install pycryptodome
```
