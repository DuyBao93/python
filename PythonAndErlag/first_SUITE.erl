- module (first_SUITE).
- import(lists,[nth/2]).
- compile(export_all).

test_001(_Config) ->
    TestCase = "Test case 002",
    ct:pal("Run testcase: ~p~n", [TestCase]),
    Expect = 15,
    Result = 
        case test_fun(1) of
            Expect -> 
                io:format("Test case passed!"),
                ct:pal("Test case passed!");
            A ->
                io:format("Res: ~p~n", [A]),
                ct:pal("Test case failed!"),
                nok
        end,
    ok = Result.

test_002(_Config) ->
    TestCase = "Test case 002",
    ct:pal("Run testcase: ~p~n", [TestCase]),
    Expect = 7,
    Result = 
        case test_fun(2) of
            Expect -> 
                io:format("Test case passed!"),
                ct:pal("Test case passed!");
            A ->
                io:format("Res: ~p~n", [A]),
                ct:pal("Test case failed!"),
                nok
        end,
    ok = Result.

test_003(_Config) ->
    TestCase = "Test case 002",
    ct:pal("Run testcase: ~p~n", [TestCase]),
    Expect = 55,
    Result = 
        case test_fun(3) of
            Expect -> 
                io:format("Test case passed!"),
                ct:pal("Test case passed!");
            A ->
                io:format("Res: ~p~n", [A]),
                ct:pal("Test case failed!"),
                nok
        end,
    ok = Result.

test_004(_Config) ->
    TestCase = "Test case 002",
    ct:pal("Run testcase: ~p~n", [TestCase]),
    Expect = 15,
    Result = 
        case test_fun(4) of
            Expect -> 
                io:format("Test case passed!"),
                ct:pal("Test case passed!");
            A ->
                io:format("Res: ~p~n", [A]),
                ct:pal("Test case failed!"),
                nok
        end,
    ok = Result.

test_005(_Config) ->
    TestCase = "Test case 002",
    ct:pal("Run testcase: ~p~n", [TestCase]),
    Expect = 231,
    Result = 
        case test_fun(5) of
            Expect -> 
                io:format("Test case passed!"),
                ct:pal("Test case passed!");
            A ->
                io:format("Res: ~p~n", [A]),
                ct:pal("Test case failed!"),
                nok
        end,
    ok = Result.

test_fun(I) ->
    Path = "e:/PythonAndErlag",
    %%% change file name 
    CurrentFile = Path ++ "/sum.txt",
    {ok, File} = file:open(CurrentFile, [read]),
    {ok , Data} = file:read(File , 1024 * 1024),
    DataList = [ element(1, string:to_integer(Substr)) || Substr <- string:tokens(Data, ", ")],
    nth(I,DataList).

suite() ->
    [].

groups() ->
    [ {group_1, [], testcase1()},
      {group_2, [], testcase2()}].

testcase1() ->
    [test_001 , test_002].

testcase2() ->
    [test_003 , test_004 , test_005].

all() ->
    [{group, all}].

init_per_suite(Config) ->
    Config.

end_per_suite(Config) ->
    Config.

init_per_group(Group, _Config) ->
    ct:comment("Group ~p starting", [Group]).

end_per_group(Group, _Config) ->
    ct:comment("Group ~p finished", [Group]).

init_per_testcase(_TestCase, Config) ->
    ct:pal("Running Init_per_testcase~n"),
    Config.

end_per_testcase(_TestCase, _Config) ->
    ct:pal("Running End_per_testcase~n"),
    ok.
