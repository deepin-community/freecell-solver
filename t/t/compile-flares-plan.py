#!/usr/bin/env python3

# TEST:source "$^CURRENT_DIRNAME/../lib/FC_Solve/__init__.py"
import unittest
from FC_Solve import FC_Solve_Suite


class MyTests(unittest.TestCase):
    def test_null_plan(self):
        fcs = FC_Solve_Suite(self)

        name = "null plan"

        # TEST*$compile_flares_plan_ok
        fcs.compile_flares_plan_ok(name, None)

        # TEST
        fcs.flare_plan_num_items_is(name, 2)

        # TEST*$flare_plan_item_is_run_indef
        fcs.flare_plan_item_is_run_indef(name, 0, 0)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(name + " No. 1", 1)

    def test_empty_plan(self):
        fcs = FC_Solve_Suite(self)

        name = "empty string plan"

        # TEST*$compile_flares_plan_ok
        fcs.compile_flares_plan_ok(name, "")

        # TEST
        fcs.flare_plan_num_items_is(name, 2)

        # TEST*$flare_plan_item_is_run_indef
        fcs.flare_plan_item_is_run_indef(name, 0, 0)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(name + " No. 1", 1)

    def test_two_runs(self):
        fcs = FC_Solve_Suite(self)

        name = "Two Run's"
        # TEST*$input_cmd_line
        fcs.input_cmd_line(
            "Input Flares",
            ["--flare-name", "dfs", "-nf",
             "--flare-name", "befs", "--method", "a-star"])

        # TEST*$compile_flares_plan_ok
        fcs.compile_flares_plan_ok(name, "Run:500@befs,Run:1500@dfs")

        # 2 runs and then the implicit checkpoint.
        # TEST
        fcs.flare_plan_num_items_is(name, 3)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(name + " No. 0", 0, 1, 500)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(name + " No. 1", 1, 0, 1500)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(name + " No. 2", 2)

    def test_with_checkpoints(self):
        testname = "With checkpoints"

        fcs = FC_Solve_Suite(self)

        # TEST*$input_cmd_line
        fcs.input_cmd_line(
            "Input Flares",
            ["--flare-name", "dfs", "-nf",
             "--flare-name", "befs", "--method", "a-star", "-nf",
             "--flare-name", "foo", "--method", "a-star",
                "-asw", "0.2,0.3,0.5,0,0", "-nf",
             "--flare-name", "bar", "-to", "[01][23467]",
             ])

        # TEST*$compile_flares_plan_ok
        fcs.compile_flares_plan_ok(
            testname,
            "Run:500@dfs,Run:300@bar,CP:,Run:1000@befs"
        )

        # 4 items and then the implicit checkpoint.
        # TEST
        fcs.flare_plan_num_items_is(testname, 5)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 0" % (testname)), 0, 0, 500)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 1" % (testname)), 1, 3, 300)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(("%s No. 2" % (testname)), 2)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 3" % (testname)), 3, 1, 1000)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(("%s No. 4" % (testname)), 4)

    def test_with_checkpoints_and_explicit_checkpoint(self):
        testname = "With checkpoints with explicit checkpoint at end."

        fcs = FC_Solve_Suite(self)

        # TEST*$input_cmd_line
        fcs.input_cmd_line(
            "Input Flares",
            ["--flare-name", "dfs", "-nf",
             "--flare-name", "befs", "--method", "a-star", "-nf",
             "--flare-name", "foo", "--method", "a-star",
                "-asw", "0.2,0.3,0.5,0,0", "-nf",
             "--flare-name", "bar", "-to", "[01][23467]",
             ])

        # TEST*$compile_flares_plan_ok
        fcs.compile_flares_plan_ok(
            testname,
            "Run:500@dfs,Run:300@bar,CP:,Run:1000@befs,CP:"
        )

        # 5 items (without an extra and redundant explicit
        # checkpoint at the end.)
        # TEST
        fcs.flare_plan_num_items_is(testname, 5)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 0" % (testname)), 0, 0, 500)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 1" % (testname)), 1, 3, 300)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(("%s No. 2" % (testname)), 2)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 3" % (testname)), 3, 1, 1000)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(("%s No. 4" % (testname)), 4)

    def test_with_run_indef(self):
        testname = "With RunIndef"

        fcs = FC_Solve_Suite(self)

        # TEST*$input_cmd_line
        fcs.input_cmd_line(
            "Input Flares",
            ["--flare-name", "dfs", "-nf",
             "--flare-name", "befs", "--method", "a-star", "-nf",
             "--flare-name", "foo", "--method", "a-star",
                "-asw", "0.2,0.3,0.5,0,0", "-nf",
             "--flare-name", "bar", "-to", "[01][23467]",
             ])

        # TEST*$compile_flares_plan_ok
        fcs.compile_flares_plan_ok(
            testname,
            "Run:500@dfs,Run:300@bar,CP:,RunIndef:befs"
        )

        # 5 items (with an extra implicit chechpoint at the end).
        # TEST
        fcs.flare_plan_num_items_is(testname, 5)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 0" % (testname)), 0, 0, 500)

        # TEST*$flare_plan_item_is_run
        fcs.flare_plan_item_is_run(("%s No. 1" % (testname)), 1, 3, 300)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(("%s No. 2" % (testname)), 2)

        # TEST*$flare_plan_item_is_run_indef
        fcs.flare_plan_item_is_run_indef(("%s No. 3" % (testname)), 3, 1)

        # TEST*$flare_plan_item_is_checkpoint
        fcs.flare_plan_item_is_checkpoint(("%s No. 4" % (testname)), 4)


if __name__ == "__main__":
    # plan(73)
    from pycotap import TAPTestRunner
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    TAPTestRunner().run(suite)
