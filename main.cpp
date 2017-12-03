#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstdlib>
#include <string>
#include <utility>

#include "Random.h"
#include "Point.h"

using namespace std;

bool isEqual(Point a, Point b){
	return (a.x == b.x) && (a.y == b.y);
}

int main(int argc, char* argv[]){
	int i, j, size = atoi(argv[1]), k;
	int miny = atoi(argv[2]), maxy = atoi(argv[3]), minx = atoi(argv[4]), maxx = atoi(argv[5]), maxEdges = atoi(argv[6]);
	int first, second;
	bool remove;
	vector<pair<Point, Point> > edges;
	vector<Point> points;
	vector<float> costs;
	string fname;
	ofstream out;
	
	Random::init();
	
	for(i = 0; i < size; i++){
		points.push_back(Point(Random::intInRange(minx, maxx), Random::intInRange(miny, maxy), 0));
	}

	j = 0;
	for(auto it = points.begin(); it != points.end(); j++){
		remove = false;
		size = points.size();
		for(i = 0; i < size; i++){
			if(i != j && (*it).x == points[i].x && (*it).y == points[i].y){
				remove = true;
				break;
			}
		}	
		if(remove){
			it = points.erase(it);
			remove = !remove;
		}else{
			it++;
		}
	}
	
	size = points.size();
	for(i = 0; i < maxEdges; i++){
		first = Random::intInRange(0, size);
		second = Random::intInRange(0, size);
		
		while(first == second) second = Random::intInRange(0, size);
		
		edges.push_back(make_pair(points[first], points[second]));
		
		j = edges.size()-1;
		for(auto it = edges.begin(); it != edges.end()-1; ){
			if((*it).first.x == edges[j].first.x && (*it).first.y == edges[j].first.y && (*it).second.x == edges[j].second.x && (*it).second.y == edges[j].second.y){
				it = edges.erase(it);
			}else{
				it++;
			}
		}
	}
	
	costs.resize(edges.size());
	
	size = edges.size();
	for(i = 0; i < size; i++){
		costs[i] = edges[i].first.distance(edges[i].second) + Random::floatInRange(0.0, 100.0);
	}	
	
	fname = to_string(edges.size()) + string(".inst");
	out.open(fname);	
	
	for(i = 0; i < edges.size(); i++){
		out << edges[i].first.x << " " << edges[i].first.y << " " << edges[i].second.x << " " << edges[i].second.y << " " << costs[i] << endl;
	}
	
	cout << fname << endl;
	
	out.close();
}
