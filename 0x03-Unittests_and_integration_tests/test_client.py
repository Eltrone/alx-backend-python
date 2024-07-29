#!/usr/bin/env python3
"""Module for testing GithubOrgClient."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mocked_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        json_payload = {"name": org_name}
        mocked_get_json.return_value = json_payload
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, json_payload)
        mocked_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property."""
        json_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = json_payload
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client._public_repos_url, json_payload["repos_url"])

if __name__ == '__main__':
    unittest.main()
