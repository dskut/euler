
#include <iostream>
#include <fstream>
#include <vector>

struct Coord {
    int row;
    int column;

    Coord(int row = 0, int column = 0)
        : row(row), column(column)
    {}

    bool isValid() const {
        return row >= 0 && column >= 0;
    }
};

const Coord startCoord;

class Sudoku {
public:
    void addRow(const std::string& line) {
        std::vector<int> row;
        for (char c: line) {
            row.push_back(c - 48);
        }
        cells_.push_back(row);
    }

    bool solve(Coord coord = startCoord) {
        coord = findNextZero(coord);
        if (!coord.isValid()) {
            return true;
        }
        for (int i = 1; i <= 9; ++i) {
            if (!existsInRow(coord.row, i) && !existsInColumn(coord.column, i)
                    && !existsInUnit(coord, i)) {
                cells_[coord.row][coord.column] = i;
                if (solve(coord)) {
                    return true;
                }
            }
        }
        cells_[coord.row][coord.column] = 0;
        return false;
    }

    void print() const {
        for (size_t i = 0; i < cells_.size(); ++i) {
            if (i % 3 == 0 && i > 0) {
                std::cout << std::endl; 
            }
            for (size_t j = 0; j < cells_[i].size(); ++j) {
                if (j % 3 == 0 && j > 0) {
                    std::cout << ' ';
                }
                std::cout << cells_[i][j];
            }
            std::cout << std::endl; 
        }
    }

    int getTopLeft() const {
        auto& row = cells_[0];
        return row[0]*100 + row[1]*10 + row[2];
    }

private:
    Coord findNextZero(const Coord& coord) const {
        for (size_t i = coord.row; i < cells_.size(); ++i) {
            for (size_t j = 0; j < cells_[i].size(); ++j) {
                if (cells_[i][j] == 0) {
                    return Coord(i, j);
                }
            }
        }
        return Coord(-1, -1);
    }

    bool existsInRow(int row, int x) const {
        for (size_t i = 0; i < cells_[row].size(); ++i) {
            if (cells_[row][i] == x) {
                return true;
            }
        }
        return false;
    }

    bool existsInColumn(int column, int x) const {
        for (size_t i = 0; i < cells_.size(); ++i) {
            if (cells_[i][column] == x) {
                return true;
            }
        }
        return false;
    }

    bool existsInUnit(const Coord& coord, int x) const {
        int unitRow = coord.row / 3;
        int unitColumn = coord.column / 3;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int c = cells_[unitRow*3 + i][unitColumn*3 + j];
                if (c == x) {
                    return true;
                }
            }
        }
        return false;
    }

    std::vector<std::vector<int>> cells_;
};

std::vector<Sudoku> readSudokus(const std::string& filename) {
    std::ifstream stream(filename);
    std::string line;
    std::vector<Sudoku> res;
    while (getline(stream, line)) {
        Sudoku sudoku;
        for (size_t i = 0; i < 9; ++i) {
            getline(stream, line);
            sudoku.addRow(line);
        }
        res.push_back(sudoku);
    }
    return res;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cout << "usage: " << argv[0] << " sudoku.txt" << std::endl;
        return 1;
    }
    const std::string filename = argv[1];
    std::vector<Sudoku> sudokus = readSudokus(filename);
    for (auto& sudoku: sudokus) {
        sudoku.solve();
        std::cout << "------------" << std::endl;
        sudoku.print();
    }
    int res = 0;
    for (const auto& sudoku: sudokus) {
        res += sudoku.getTopLeft();
    }
    std::cout << res << std::endl;
    return 0;
}
