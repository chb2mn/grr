#!/usr/bin/env python
from absl import app
from absl.testing import absltest

from grr_response_server.databases import db_clients_test
from grr_response_server.databases import mysql_test
from grr.test_lib import test_lib


class MysqlClientsTest(db_clients_test.DatabaseTestClientsMixin,
                       mysql_test.MysqlTestBase, absltest.TestCase):

  # TODO: Enforce foreign key constraint on the `users` table.
  def testMultiAddClientLabelsUnknownUser(self):
    self.skipTest("Foreign key constraint on the `users` table not enforced.")
    super().testMultiAddClientLabelsUnknownUser()


if __name__ == "__main__":
  app.run(test_lib.main)
