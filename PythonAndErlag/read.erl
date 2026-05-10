-module(read).
-import(lists,[nth/2]).
-export([parse_file/1]).


parse_file(FN) ->
    file:open(FN, [read]).
    % {ok , Data} = file:read(File , 1024 * 1024),
    % DataList = [ element(1, string:to_integer(Substr)) || Substr <- string:tokens(Data, ", ")],
    % DataList,
    % nth(1,DataList) * 2.

% firsts([]) -> [];

% firsts([Tuple|Tuples]) ->
%     {Name} = Tuple,
%     [Name | firsts(Tuples)].