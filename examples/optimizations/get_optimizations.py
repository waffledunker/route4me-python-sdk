from route4me import Route4Me

KEY = "11111111111111111111111111111111"


def main():
    route4me = Route4Me(KEY)
    optimization = route4me.optimization
    response = optimization.get_optimizations(limit=10, Offset=5)
    if hasattr(response, 'errors'):
        print '. '.join(response.errors)
    else:
        print response
        for i, optimization in enumerate(response.optimizations):
            optimization_problem_id = optimization.optimization_problem_id
            print 'Optimization #{}'.format(i + 1)
            print '\tOptimization ID: {}'.format(optimization_problem_id)

if __name__ == '__main__':
    main()
