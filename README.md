# HiveBox API
A RESTful API to track environmental sensor data for beekeepers using openSenseMap data.

## Goal

The goal of this project is to build a scalable RESTful API around [openSenseMap](https://opensensemap.org/) but customized to help beekeeper with their chores. The API output should be in JSON. You will start with a basic implementation, then extend the whole system to handles thousands of requests per second.

### IDs
senseBox IDs:
1. edmonds-WA
   1. ID: 6351780cc18329001ba8d4a3
      1. 11.63
      2. 024-12-10T00:40:57.172Z
   2. https://api.opensensemap.org/boxes/6351780cc18329001ba8d4a3
   3. https://opensensemap.org/explore/6351780cc18329001ba8d4a3
2. 97tug
      1. 7.955882
      2. 2024-12-10T00:40:19.586Z
   1. ID: 63ac947f1aaa3a001b8a34bd
   2. https://api.opensensemap.org/boxes/63ac947f1aaa3a001b8a34bd
   3. https://opensensemap.org/explore/63ac947f1aaa3a001b8a34bd
3. rakwanna
      1. 4.7
      2. 024-12-10T00:40:15.616Z
   1. ID: 62abdbfbb91502001b7c05a8
   2. https://api.opensensemap.org/boxes/62abdbfbb91502001b7c05a8
   3. https://opensensemap.org/explore/62abdbfbb91502001b7c05a8




### Tasklist

**Phase 2**
- [x] Code:
  - [x] Create GitHub repository.
  - [x] Create a function that print current app version using semantic versioning with `1v0.0.1`
- [x] Containers
  - [x] Create a dockerfile, build the image and run it locally.
- [x] Test
  - [x] Run the app container and make sure it returns the correct value. 

**Phase 3**
- [x] Code:
  - [x] Version Endpoint: `/version`
    - [x] Returns the version of the deployed app.
  - [x] Temperature Endpoint: `/temperature`
    - [x] Return current average temperature based on all senseBox data.
    - [x] Ensure that the data is no older 1 hour.
- [ ] Continuous Integration
  - [x] Create a GitHub Actions workflow for CI.
  - [x] Add step to lint code and Dockerfile.
  - [x] Add step to build the Docker image.
  - [x] Add step to unit tests.
  - [ ] Setup OpenSSF Scorecard GitHub Action and fix any issues reported by it.
- [ ] Test
  - [ ] In the CI pipeline, call the /version endpoint and ensure that it returns the correct value.
- [x] [Docker Best Practices](https://tech.aabouzaid.com/2021/09/docker-best-practices-workshop-presentation.html)

### Tools

1. Docker & Dockerhub