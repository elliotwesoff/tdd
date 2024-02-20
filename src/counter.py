'''
Module for counter endpoints. All routes should begin with /counters
'''

from flask import Flask
import status
app = Flask(__name__)

COUNTERS = {}

# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".


@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info("Request to create counter: %s", name)
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a counter"""
    app.logger.info("Request to update counter: %s", name)

    if name in COUNTERS:
        COUNTERS[name] += 1
        return {name: COUNTERS[name]}, status.HTTP_200_OK

    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND


@app.route('/counters/<name>', methods=['GET'])
def get_counter(name):
    """Get a counter"""
    app.logger.info("Request to get counter: %s", name)

    if name in COUNTERS:
        return {name: COUNTERS[name]}, status.HTTP_200_OK

    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND


@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info("Request to delete counter: %s", name)

    if name in COUNTERS:
        del COUNTERS[name]
        return "NO CONTENT", status.HTTP_204_NO_CONTENT

    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND
