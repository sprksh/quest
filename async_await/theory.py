# the way to do collaboratoive multiprogramming. 
# much convinient in 3.7+ you dont have to worry about eventloop to 
# start with

# the entire chain of function should be awaitable that is async
# you can await only async functions
# while awaiting, the async function voluntarily "gives control away"/ "releases the GIL",
# and waits for the callback from the io bound task, for anyone else to take up

# the eventloop can be considered to be a list where you can submit a task.
# the eventloop will run that task and give a callback once that task is completed

import asyncio

async def some_io_bound_task_async():
    print("starting io task")
    await asyncio.sleep(1)
    # all async task need to be awaited
    print("completed io task")
    return "some value"


async def do_something_async():
    print("start await some io task")
    r = await some_io_bound_task_async()
    print("Completed await some io task. got %s" % r)

# functions starting with async are not normal functions
# they are coriutines

async def test_async():
    # this one will behave like a normal function because there is nothing to parallelize
    await do_something_async()

    # here gather will parallelize all async tasks
    await asyncio.gather(
        do_something_async(),
        do_something_async(),
        do_something_async()
    )


asyncio.run(test_async())

# semaphores (bounded) with asyncio to limit the number of tasks running in parallel
# https://quentin.pradet.me/blog/how-do-you-limit-memory-usage-with-asyncio.html