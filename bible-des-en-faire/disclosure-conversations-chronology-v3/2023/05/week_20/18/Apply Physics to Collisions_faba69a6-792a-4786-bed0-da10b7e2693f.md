# Apply Physics to Collisions

**Date de création :** 2023-05-18 14:45:48

---

**Lucie :**
After retrieving an array of collisions in 3d in typescript as { penetrationDepth: number, penetrationNormal: Vector3 }[] how can i apply physics to my object

---

**ShadeOS :**
To apply physics to your object based on the retrieved array of collisions, you can follow these general steps:

1. Iterate through each collision in the array.
2. For each collision, calculate the resolution impulse based on the penetration depth and penetration normal. The resolution impulse determines how the objects should respond to the collision.
3. Apply the resolution impulse to the object's velocity or position, depending on the type of physics simulation you are using.
4. Repeat these steps for all collisions in the array.

Here's a TypeScript code snippet that demonstrates the basic idea:

```typescript
interface Collision {
  penetrationDepth: number;
  penetrationNormal: Vector3;
}

interface Vector3 {
  x: number;
  y: number;
  z: number;
}

class PhysicsObject {
  position: Vector3;
  velocity: Vector3;
  // ... other properties and methods

  applyCollision(collisions: Collision[]) {
    for (const collision of collisions) {
      const resolutionImpulse = calculateResolutionImpulse(collision.penetrationDepth, collision.penetrationNormal);
      this.applyImpulse(resolutionImpulse);
    }
  }

  calculateResolutionImpulse(penetrationDepth: number, penetrationNormal: Vector3): Vector3 {
    // Calculate the resolution impulse based on the penetration depth and penetration normal
    // ...
    return impulse;
  }

  applyImpulse(impulse: Vector3) {
    // Apply the impulse to the object's velocity or position
    // ...
  }
}

// Usage example
const object = new PhysicsObject();
const collisions: Collision[] = /* Retrieve collisions */;
object.applyCollision(collisions);
```

Please note that the code provided is a simplified example, and the actual implementation may vary depending on your specific physics engine or requirements.

---

**Lucie :**
Can you give details of each methods you provided in your code

---

**ShadeOS :**
Certainly! Here are the details of each method provided in the code:

1. `applyCollision(collisions: Collision[])`: This method is responsible for applying physics to the object based on the array of collisions. It takes an array of `Collision` objects as input. It iterates through each collision and calls the `calculateResolutionImpulse()` method to calculate the resolution impulse. Then, it applies the impulse to the object by calling the `applyImpulse()` method.

2. `calculateResolutionImpulse(penetrationDepth: number, penetrationNormal: Vector3): Vector3`: This method calculates the resolution impulse based on the penetration depth and penetration normal of a collision. The impulse determines how the objects involved in the collision should respond. The specific calculations for the impulse will depend on the physics simulation algorithm you are using. You would need to implement this method with the appropriate physics equations and algorithms for your particular use

---

**Lucie :**
Can you give code for calculate resolutionImpulse and applyImpulse, knowing that my rigidbody is a capsule representing character

---

**ShadeOS :**
Certainly! Here's an example implementation of the `calculateResolutionImpulse()` and `applyImpulse()` methods for a capsule-shaped rigidbody representing a character:

```typescript
class PhysicsObject {
  // ...

  calculateResolutionImpulse(penetrationDepth: number, penetrationNormal: Vector3): Vector3 {
    const restitution = 0.5; // Coefficient of restitution (bounce factor)
    const velocityAlongNormal = this.velocity.x * penetrationNormal.x +
                                this.velocity.y * penetrationNormal.y +
                                this.velocity.z * penetrationNormal.z;
    const impulseMagnitude = -(1 + restitution) * velocityAlongNormal;

    const impulse = {
      x: impulseMagnitude * penetrationNormal.x,
      y: impulseMagnitude * penetrationNormal.y,
      z: impulseMagnitude * penetrationNormal.z
    };

    return impulse;
  }

  applyImpulse(impulse: Vector3) {
    // Apply the impulse to the object's velocity
    this.velocity.x += impulse.x;
    this.velocity.y += impulse.y;
    this.velocity.z += impulse.z;
  }
}

// Usage example
const object = new PhysicsObject();
// ...
```

In this example, we assume a simple linear impulse-based collision response model. The `calculateResolutionImpulse()` method calculates the magnitude of the impulse based on the velocity of the object along the collision normal. The restitution coefficient determines the bounce factor of the collision. The impulse is then applied in the direction of the collision normal.

The `applyImpulse()` method simply adds the impulse vector to the object's velocity vector. Note that this is a simplified implementation, and in a real-world scenario, you may need to consider additional factors such as mass, friction, and angular momentum, depending on your physics simulation requirements.

---

**Lucie :**
Can you add something to handle gravity and to prevent my character to fall through the ground

---

**ShadeOS :**
Certainly! To handle gravity and prevent your character from falling through the ground, you can incorporate a gravity force and perform collision detection with the ground surface. Here's an updated version of the code that includes these additions:

```typescript
const GRAVITY = -9.8; // Acceleration due to gravity

class PhysicsObject {
  // ...

  update(deltaTime: number) {
    // Apply gravity
    const gravityForce = {
      x: 0,
      y: GRAVITY,
      z: 0
    };
    this.applyForce(gravityForce, deltaTime);

    // Perform collision detection and response
    const groundHeight = 0; // Assuming the ground is at height 0
    if (this.position.y < groundHeight) {
      this.position.y = groundHeight; // Prevent falling through the ground
      this.velocity.y = 0; // Stop vertical movement upon collision with the ground
    }
  }

  applyForce(force: Vector3, deltaTime: number) {
    // Calculate acceleration based on the force and mass (assuming unit mass of 1)
    const acceleration = {
      x: force.x,
      y: force.y,
      z: force.z
    };

    // Update velocity based on acceleration and time
    this.velocity.x += acceleration.x * deltaTime;
    this.velocity.y += acceleration.y * deltaTime;
    this.velocity.z += acceleration.z * deltaTime;

    // Update position based on velocity and time
    this.position.x += this.velocity.x * deltaTime;
    this.position.y += this.velocity.y * deltaTime;
    this.position.z += this.velocity.z * deltaTime;
  }
}

// Usage example
const object = new PhysicsObject();
const deltaTime = 0.016; // Example time step (e.g., 60 FPS)
object.update(deltaTime);
// ...
```

In this updated code, the `update()` method is introduced to handle the simulation of physics over time. It applies a gravity force to the object by calling `applyForce()` with the gravity vector and the current time step (`deltaTime`). The ground height is assumed to be at `0` units. If the object's position falls below the ground, its position is clamped to the ground height, and its vertical velocity is set to `0`, preventing it from falling through the ground.

The `applyForce()` method calculates the acceleration based on the applied force and unit mass. It then updates the velocity and position of the object based on the calculated acceleration, time, and the current object's velocity.

Remember to adjust the gravity value (`GRAVITY`) according to your specific needs and units of measurement. Additionally, this code assumes a simplified scenario with a fixed ground height. In a more complex scenario, you may need a more sophisticated collision detection and response system.

---

**Lucie :**
Add to this code a logic to handle gravity:

class PhysicsObject {
  // ...
applyCollision(collisions: Collision[]) {
    for (const collision of collisions) {
      const resolutionImpulse = calculateResolutionImpulse(collision.penetrationDepth, collision.penetrationNormal);
      this.applyImpulse(resolutionImpulse);
    }
  }
  calculateResolutionImpulse(penetrationDepth: number, penetrationNormal: Vector3): Vector3 {
    const restitution = 0.5; // Coefficient of restitution (bounce factor)
    const velocityAlongNormal = this.velocity.x * penetrationNormal.x +
                                this.velocity.y * penetrationNormal.y +
                                this.velocity.z * penetrationNormal.z;
    const impulseMagnitude = -(1 + restitution) * velocityAlongNormal;

    const impulse = {
      x: impulseMagnitude * penetrationNormal.x,
      y: impulseMagnitude * penetrationNormal.y,
      z: impulseMagnitude * penetrationNormal.z
    };

    return impulse;
  }

  applyImpulse(impulse: Vector3) {
    // Apply the impulse to the object's velocity
    this.velocity.x += impulse.x;
    this.velocity.y += impulse.y;
    this.velocity.z += impulse.z;
  }
}

// Usage example
const object = new PhysicsObject();
// ...

---

**ShadeOS :**
To handle gravity in the given code, you can add an additional step in the `applyForce()` method to include the effect of gravity on the object's velocity. Here's the updated code with the gravity logic:

```typescript
const GRAVITY = -9.8; // Acceleration due to gravity

class PhysicsObject {
  // ...

  applyForce(force: Vector3, deltaTime: number) {
    // Calculate acceleration based on the force and mass (assuming unit mass of 1)
    const acceleration = {
      x: force.x,
      y: force.y + GRAVITY, // Include gravity in the y-axis acceleration
      z: force.z
    };

    // Update velocity based on acceleration and time
    this.velocity.x += acceleration.x * deltaTime;
    this.velocity.y += acceleration.y * deltaTime;
    this.velocity.z += acceleration.z * deltaTime;

    // Update position based on velocity and time
    this.position.x += this.velocity.x * deltaTime;
    this.position.y += this.velocity.y * deltaTime;
    this.position.z += this.velocity.z * deltaTime;
  }
}

// Usage example
const object = new PhysicsObject();
// ...
```

In this updated code, the `applyForce()` method is modified to include the effect of gravity in the y-axis acceleration. The gravity force is added to the y-component of the applied force. The acceleration is then used to update the velocity and position of the object.

Make sure to adjust the `GRAVITY` value according to your specific needs and units of measurement. With this addition, the object will experience the force of gravity, causing it to accelerate downwards and simulate realistic gravity behavior.

---

**Lucie :**
can you describe full detailed pseudocode of that function:

World.prototype.step = function(dt, timeSinceLastCalled, maxSubSteps)

from the git https://schteppe.github.io/cannon.js/

---

**ShadeOS :**
Certainly! Here's a detailed pseudocode description of the `step` function in the `World` class from the Cannon.js library:

```
World.prototype.step = function(dt, timeSinceLastCalled, maxSubSteps) {
  // Step 1: Preprocessing
  Emit 'preStep' event

  // Step 2: Integration and collision detection
  Calculate the total number of substeps required:
    subSteps = Math.ceil(timeSinceLastCalled / dt)

  if (subSteps > maxSubSteps)
    subSteps = maxSubSteps

  for (i = 0; i < subSteps; i++) {
    // Calculate the time of this substep
    t = i / subSteps * dt

    // Emit 'preStep' event at each substep
    Emit 'preStep' event

    // Apply all external forces to the bodies
    Apply external forces to bodies

    // Integrate positions
    Integrate positions of bodies using symplectic Euler

    // Update collision detection structures
    Update collision detection structures

    // Perform broadphase collision detection
    Perform broadphase collision detection

    // Perform narrowphase collision detection
    Perform narrowphase collision detection

    // Solve contact constraints
    Solve contact constraints

    // Solve friction constraints
    Solve friction constraints

    // Integrate velocities
    Integrate velocities of bodies

    // Clear applied force and torque on bodies
    Clear applied forces and torques on bodies

    // Emit 'postStep' event at each substep
    Emit 'postStep' event
  }

  // Step 3: Postprocessing
  Emit 'postStep' event

  // Step 4: Update sleeping state of bodies
  Update sleeping state of bodies

  // Step 5: Emit 'end' event
  Emit 'end' event
}
```

This pseudocode describes the main steps involved in the `step` function of the `World` class in Cannon.js. Here's a breakdown of each step:

1. Preprocessing: Emit the 'preStep' event.

2. Integration and collision detection:
   - Calculate the number of substeps based on the provided time interval and maximum substeps.
   - For each substep:
     - Calculate the time of the substep.
     - Emit the 'preStep' event.
     - Apply external forces to the bodies.
     - Integrate the positions of the bodies using the symplectic Euler method.
     - Update the collision detection structures.
     - Perform broadphase collision detection.
     - Perform narrowphase collision detection.
     - Solve contact constraints.
     - Solve friction constraints.
     - Integrate the velocities of the bodies.
     - Clear the applied forces and torques on the bodies.
     - Emit the 'postStep' event.

3. Postprocessing: Emit the 'postStep' event.

4. Update the sleeping state of bodies.

5. Emit the 'end' event.

This pseudocode gives an overview of the steps performed in the `step` function of the Cannon.js library's `World` class. The actual implementation may include additional details and optimizations, but this should provide a general understanding of the process.
