
local function read_file_into_lines(filename)
    local lines = {}
    for line in io.lines(filename) do
        table.insert(lines, line)
    end
    return lines
end

local function save_1(lines)
    local start = 50
    local result = 0
    for i, v in ipairs(lines) do
        local direction = string.sub(v, 1, 1)
        local steps = tonumber(string.sub(v, 2))
        if direction == "L" then
            start = ((start - steps) + 100) % 100
        elseif direction == "R" then
            start = ((start + steps) + 100) % 100
        end
        if start == 0 then
            result = result + 1
        end
    end
    return result
end

local function save_2(lines)
    local start = 50
    local result = 0
    for _, v in ipairs(lines) do
        local direction = string.sub(v, 1, 1)
        local steps = tonumber(string.sub(v, 2))
        local old_start = start
        local next_start
        if direction == "L" then
            for i = 1, steps do
                if ((old_start - i) % 100) == 0 then
                    result = result + 1
                end
            end
            next_start = old_start - steps
        elseif direction == "R" then
            for i = 1, steps do
                if ((old_start + i) % 100) == 0 then
                    result = result + 1
                end
            end
            next_start = old_start + steps
        end
        start = next_start % 100
    end
    return result
end

local test = "test.txt"
local input = "input.txt"
local lines = read_file_into_lines(input)
print(save_2(lines))
