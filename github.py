import requests

GITHUB_API_URL = "https://api.github.com/graphql"

QUERY = """
query($repository_owner:String!, $repository_name: String!, $count: Int!) {
  repository(
    owner: $repository_owner,
    name: $repository_name) {
    
    refs(last: $count,refPrefix:"refs/tags/") {
      edges {
        node{
          name
        }
      }
    }
    
    releases(last: $count) {
      edges {
        node {
          name
        }
      }
    }
  }
}
"""

class Github:

    def __authorization_header(self):
        return "token " + self.token

    def __request_headers(self):
        return {
            'authorization': self.__authorization_header(),
        }

    def __init__(self, token):
        self.token = token

    def getTagsAndReleases(self, repository_owner, repository_name, count):
        payload = {"query": QUERY,
                   "variables": {
                       "repository_owner": repository_owner,
                       "repository_name": repository_name,
                       "count": count
                   }}
        print "Requesting for", repository_name
        response = requests.post(GITHUB_API_URL, json=payload, headers=self.__request_headers())
        print "Got status code for", repository_name, response.status_code
        return response.json()