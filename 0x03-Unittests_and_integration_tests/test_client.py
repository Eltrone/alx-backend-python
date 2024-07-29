#!/usr/bin/env python3
"""Unit tests for client module."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """Test that org returns correct value."""
        url = f"https://api.github.com/orgs/{org_name}"
        client = GithubOrgClient(org_name)
        client.org()
        mock_get.assert_called_once_with(url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property."""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/org/repos"}
        client = GithubOrgClient("org")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/org/repos")

    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """Test public_repos method."""
        mock_public_repos_url.return_value = "https://api.github.com/orgs/org/repos"
        mock_get_json.return_value = [{"name": "repo"}]
        client = GithubOrgClient("org")
        self.assertEqual(client.public_repos(), ["repo"])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Setup for integration tests."""
        cls.get_patcher = patch('requests.get')
        cls.mock = cls.get_patcher.start()
        cls.mock.side_effect = [
            {"json": lambda: cls.org_payload},
            {"json": lambda: cls.repos_payload}
        ]

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos with integration."""
        client = GithubOrgClient("org")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

if __name__ == '__main__':
    unittest.main()
